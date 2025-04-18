<template>
  <div>
    <Header/>
    <PageHeader :title="blog.title"/>
    <BlogDetails :blog="blog" :new-blogs="newBlogs"/>
    <Footer/>
  </div>
</template>
<script>
import Header from "~/components/Header.vue";
import PageHeader from "~/components/PageHeader.vue";
import BlogDetails from "~/components/BlogDetails.vue";
import Footer from "~/components/Footer.vue";
import BlogHome from "~/components/BlogHome.vue";
import Strapi from "strapi-sdk-javascript";

export default {
  components: {
    BlogHome,
    Header,
    PageHeader,
    BlogDetails,
    Footer
  },
  head() {
    return {
      title: "Dimon | Blog Details"
    }
  },
  async asyncData({$config, params, error}) {
    try {
      const apiBase = $config.API_BASE;
      const collection = 'blogs';
      const slug = params.slug;
      if (!params.slug) {
        throw new Error('缺少参数[slug]');
      }

      let apiUrl, queryParams;

      apiUrl = `${apiBase}/${collection}`;
      queryParams = {
        'filters[slug][$eq]': slug,
        'populate': '*', // 加载关联内容
      };

      const queryString = new URLSearchParams(queryParams).toString();
      const urlWithQuery = `${apiUrl}?${queryString}`;
      const response = await fetch(urlWithQuery);
      // 🔥处理HTTP状态码错误（4xx/5xx等）
      if (!response.ok) {
        throw new Error(`服务器错误: ${response.status}`);
      }
      const dataRaw = await response.json();
      const blog = dataRaw.data?.[0]?.attributes;

      if (!blog) {
        console.error(`找不到匹配的文章 ➜ slug=${slug}`);
        error({statusCode: 404, message: '无法找到这篇内容'});
        return; // 提前终止
      }

      const strapi = new Strapi($config.API_BASE);
      const newBlogs = await strapi.getEntries('blogs', {
        populate: "*", pagination: {
          pageSize: 3,
          page: 1,
        }
      });

      return {blog, newBlogs};

    } catch (err) {
      error({statusCode: err.response?.status || 500})
    }
  },
  beforeRouteUpdate(to, from, next) {
    this.$nuxt.refresh();  // 强制刷新页面，重新调用 asyncData
    next();
  },
}
</script>
