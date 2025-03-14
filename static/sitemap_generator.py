import requests
from datetime import datetime
import xml.etree.ElementTree as ET
from xml.dom import minidom
import gzip
import os
import logging

# 配置参数
CONFIG = {
    "strapi_base_url": "http://newcms.dingdang.tw/api",
    "site_url": "https://dingdang.tw",
    "output_path": "/www/wwwroot/dingdang.tw/nuxt-dingdang/static/sitemapAreaCode.xml",  # 网站地图输出路径
    "static_routes": ["/", "/check", "/area-code", "/download","/blog"],
    "content_types": {
        "areas": {
            "url_pattern": "/city/{name_en}?country={country}",  # 修改为带有查询参数
            "field_path": ["attributes", "json"],  # 字段层级（根据实际数据结构调整）
            "filters": {"filters[type][$eq]": "countrys"}  # 添加过滤条件
        },
        "blogs": {
            "url_pattern": "/blogs/{slug}",
            "field_path": ["attributes", "slug"],  # 直接取 attributes.slug
        }
    },
    "sitemap_settings": {
        "changefreq": "daily",
        "priority": 0.8
    }
}

# 日志配置
logging.basicConfig(
    filename='sitemap_generator.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def fetch_all_strapi_data(content_type, filters=None):
    """分页获取 Strapi 过滤后的数据"""
    items = []
    page = 1

    while True:
        try:
            params = {
                "populate":"*",
                "pagination[page]": page,
                "pagination[pageSize]": 100,
                "sort": "updatedAt:desc"
            }
            if filters:
                params.update(filters)  # 添加过滤参数

            response = requests.get(
                f"{CONFIG['strapi_base_url']}/{content_type}",
                params=params,
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            items.extend(data.get('data', []))

            # 分页终止条件
            pagination = data.get('meta', {}).get('pagination', {})
            if page >= pagination.get('pageCount', 1):
                break
            page += 1
        except Exception as e:
            print(f"获取 {content_type} 数据失败: {str(e)}")
            logging.error(f"获取 {content_type} 数据失败: {str(e)}")
            break
    return items


def get_nested_field(data, path):
    """根据 path 获取嵌套字段的值，并返回所有符合条件的字段"""
    current = data
    for key in path:
        if isinstance(current, dict):
            current = current.get(key)
        elif isinstance(current, list):
            # 如果是列表，取每个元素对应的字段
            current = [item.get(key) if isinstance(item, dict) else None for item in current]
        else:
            return None

    # 如果 current 是一个列表，直接返回列表中的每个元素
    if isinstance(current, list):
        return current
    return current


def generate_sitemap():
    try:
        urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

        # 添加静态路由
        for route in CONFIG['static_routes']:
            url = ET.SubElement(urlset, "url")
            ET.SubElement(url, "loc").text = f"{CONFIG['site_url']}{route}"
            ET.SubElement(url, "lastmod").text = datetime.now().isoformat()
            ET.SubElement(url, "changefreq").text = "weekly"
            ET.SubElement(url, "priority").text = "1.0"

        # 用于去重 tags
        unique_tags = set()

        # 遍历动态路由
        for content_type, config in CONFIG['content_types'].items():
            filters = config.get("filters", {})
            items = fetch_all_strapi_data(content_type, filters)

            for item in items:
                attributes = item.get("attributes", {})

                # 处理 `/blogs/{slug}`
                if content_type == 'blogs':
                    slug = attributes.get('slug')
                    if slug:
                        full_url = CONFIG['site_url'] + config['url_pattern'].format(slug=slug)
                        url = ET.SubElement(urlset, "url")
                        ET.SubElement(url, "loc").text = full_url
                        ET.SubElement(url, "lastmod").text = attributes.get('updatedAt', datetime.now().isoformat())

                    # 处理 tags
                    tags_data = attributes.get("tags", {}).get("data", [])
                    print(f"tags_data:{tags_data}")
                    for tag in tags_data:
                        tag_name = tag.get("attributes").get("tag_name")
                        print(tag_name)
                        if tag_name:
                            unique_tags.add(tag_name)  # 自动去重

                # 处理 `/city/{name_en}?country={country}`
                if content_type == 'areas':
                    json_data = attributes.get("json", [])
                    if isinstance(json_data, list):
                        for area in json_data:  # 遍历每个地区
                            name = area.get("name")
                            name_en = area.get("name_en")
                            if name and name_en:
                                full_url = f"{CONFIG['site_url']}/city/{name_en}?country={name}"
                                url = ET.SubElement(urlset, "url")
                                ET.SubElement(url, "loc").text = full_url
                                ET.SubElement(url, "lastmod").text = attributes.get('updatedAt',
                                                                                    datetime.now().isoformat())

        # 生成 `/blog-detail/{tags}`
        for tag in unique_tags:
            # print(f"blog-detail:{tag}")
            full_url = f"{CONFIG['site_url']}/blog?tag={tag}"
            url = ET.SubElement(urlset, "url")
            ET.SubElement(url, "loc").text = full_url
            ET.SubElement(url, "lastmod").text = datetime.now().isoformat()

        # 生成格式化 XML
        xml_str = ET.tostring(urlset, encoding='utf-8')
        parsed_xml = minidom.parseString(xml_str)
        pretty_xml = parsed_xml.toprettyxml(indent="  ", encoding='utf-8')

        # 写入文件
        with open(CONFIG['output_path'], 'wb') as f:
            f.write(pretty_xml)

        print(f"成功生成 {len(urlset)} 条 URL 到 {CONFIG['output_path']}")
        logging.info(f"成功生成 {len(urlset)} 条 URL 到 {CONFIG['output_path']}")
        return True
    except Exception as e:
        print(e)
        logging.critical(f"生成网站地图失败: {str(e)}")
        return False

if __name__ == "__main__":
    generate_sitemap()