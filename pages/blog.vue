<template>
  <div>
    <HeaderTwo />
    <PageHeader title="Blog Page" />
    <Blog :blogs="blogs"/>
    <Footer />
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
    async asyncData({ error }) {
      try {
        // 使用 Strapi SDK 获取数据
        const strapi = new Strapi('http://localhost:1337');
        const blogs = await strapi.getEntries('blogs');  // 获取博客列表数据
        return { blogs };  // 返回获取的数据
      } catch (err) {
        console.error('Strapi API 请求失败:', err);
        error({ statusCode: 404, message: 'Page not found' });
      }
    },
    head(){
      return {
        title: "Dimon | Blog"
      }
    }
  }
</script>
