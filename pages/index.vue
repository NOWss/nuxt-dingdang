<template>
  <div>
    <HeaderTwo />
    <BannerTwo />
    <Features />
    <CallToActionTwo />
    <CallToAction />
    <Pricing />
    <Testimonial />
<!--    <Brands />-->
    <Counter />
    <Screenshots />
    <Faq />
    <BlogHome :blogs="blogs" />
<!--    <Subscribe />-->
    <Footer />
  </div>
</template>
<script>
  import HeaderTwo from "~/components/HeaderTwo.vue";
  import BannerTwo from "~/components/BannerTwo.vue";
  import Features from "~/components/Features.vue";
  import CallToAction from "~/components/CallToAction.vue";
  import CallToActionTwo from "~/components/CallToActionTwo.vue";
  import Pricing from "~/components/Pricing.vue";
  import Testimonial from "~/components/Testimonial.vue";
  import Brands from "~/components/Brands.vue";
  import Counter from "~/components/Counter.vue";
  import Screenshots from "~/components/Screenshots.vue";
  import Faq from "~/components/Faq.vue";
  import BlogHome from "~/components/BlogHome.vue";
  import Subscribe from "~/components/Subscribe.vue";
  import Footer from "~/components/Footer.vue";
  import Strapi from "strapi-sdk-javascript";
  export default {
    components: {
      HeaderTwo,
      BannerTwo,
      Features,
      CallToAction,
      CallToActionTwo,
      Pricing,
      Testimonial,
      Brands,
      Counter,
      Screenshots,
      Faq,
      BlogHome,
      Subscribe,
      Footer,

    },
    async asyncData({ $config }) {
      try {
        // 使用 Strapi SDK 获取数据
        const strapi = new Strapi($config.API_BASE);
        const blogs = await strapi.getEntries('blogs');  // 获取博客列表数据
        return { blogs:blogs.data };  // 返回获取的数据
      } catch (err) {
        console.error('Strapi API 请求失败:', err);
      }
    },
    head(){
      return {
        title: "Home 2 | Vue Nuxt Software App Landing Page Template"
      }
    }
  }
</script>
