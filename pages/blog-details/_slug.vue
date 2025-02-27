<template>
  <div>
    <HeaderTwo/>
    <PageHeader :title="blog.title"/>
    <BlogDetails :blog="blog"/>
    <Footer/>
  </div>
</template>
<script>
import HeaderTwo from "~/components/HeaderTwo.vue";
import PageHeader from "~/components/PageHeader.vue";
import BlogDetails from "~/components/BlogDetails.vue";
import Footer from "~/components/Footer.vue";
import BlogHome from "~/components/BlogHome.vue";

export default {
  components: {
    BlogHome,
    HeaderTwo,
    PageHeader,
    BlogDetails,
    Footer
  },
  head() {
    return {
      title: "Dimon | Blog Details"
    }
  },
  async asyncData({$config, params, error}){
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

      return {blog};

    } catch (err) {
      error({statusCode: err.response?.status || 500})
    }
  }
}
</script>
