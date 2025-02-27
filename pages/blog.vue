<template>
  <div>
    <HeaderTwo/>
    <PageHeader :title="$route.query.tag ? $route.query.tag : '新闻列表'"/>
    <Blog :blogs="blogs" :pageCount="pageCount"/>
    <Footer/>
  </div>
</template>
<script>
import HeaderTwo from "~/components/HeaderTwo.vue";
import PageHeader from "~/components/PageHeader.vue";
import Blog from "~/components/Blog.vue";
import Footer from "~/components/Footer.vue";
import Strapi from 'strapi-sdk-javascript'

export default {
  components: {
    HeaderTwo,
    PageHeader,
    Blog,
    Footer,
  },
  data() {
    return {
      page: 1,
      pageCount: 1
    }
  },
  mounted() {
    this.pageCount = Math.ceil(this.blogs.meta.pagination.total / this.blogs.meta.pagination.pageSize)
  },
  async asyncData({$config, query, error}) {
    try {
      let blogs;
      if (!query.tag) {
        // 使用 Strapi SDK 获取数据
        const strapi = new Strapi($config.API_BASE);
        blogs = await strapi.getEntries('blogs', {
          populate: "*", pagination: {
            pageSize: 2,
            page: query.page || 1
          },
        });  // 获取博客列表数据
      } else {
        const apiBase = $config.API_BASE;
        const collection = 'blogs';
        const tag = query.tag
        let apiUrl, queryParams;

        apiUrl = `${apiBase}/${collection}`;
        queryParams = {
          'filters[tags][tag_name][$eq]': tag,
          'populate': '*', // 加载关联内容
        }

        const queryString = new URLSearchParams(queryParams).toString();
        const urlWithQuery = `${apiUrl}?${queryString}`;
        console.log(`${apiUrl}?${queryString}`)
        const response = await fetch(urlWithQuery);
        // 🔥处理HTTP状态码错误（4xx/5xx等）
        if (!response.ok) {
          throw new Error(`服务器错误: ${response.status}`);
        }
        const dataRaw = await response.json();
        blogs = dataRaw;
        if (!blogs) {
          console.error(`找不到匹配的文章 ➜ slug=${slug}`);
          error({statusCode: 404, message: '无法找到这篇内容'});
          return; // 提前终止
        }
      }
      return {blogs: blogs};  // 返回获取的数据
    } catch (err) {
      console.error('Strapi API 请求失败:', err);
    }
  },
  beforeRouteUpdate(to, from, next) {
    // 检查 page 参数是否变化
    if (to.query.page !== from.query.page) {
      this.$nuxt.refresh();  // 强制刷新页面，重新调用 asyncData
    }
    next();
  },
  head() {
    return {
      title: "Dimon | Blog"
    }
  }
}
</script>
