<template>
  <div>
    <HeaderTwo/>
    <BannerTwo/>
    <Features/>
    <CallToActionTwo/>
    <CallToAction/>
    <Pricing/>
    <Testimonial/>
    <!--    <Brands />-->
    <!--    <Counter />-->
    <Screenshots/>
    <Faq/>
    <BlogHome :blogs="blogs"/>
    <Footer/>
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
    Footer,

  },
  async asyncData({$config}) {
    try {
      // 使用 Strapi SDK 获取数据
      const strapi = new Strapi($config.API_BASE);
      const blogs = await strapi.getEntries('blogs', {
        populate: "*", pagination: {
          pageSize: 6,
          page:1,
        }
      });  // 获取博客列表数据
      console.log(blogs)
      return {blogs: blogs.data};  // 返回获取的数据
    } catch (err) {
      console.error('Strapi API 请求失败:', err);
    }
  },
  head() {
    return {
      title: "叮当助手（全球号-一站式号码生成与处理平台-dingdang",
      meta: [
        {
          hid: 'keywords',
          name: 'keywords',
          content: "叮当助手，全球手机号码生成工具，号码处理软件，全球号码处理工具，号码排序乱序工具，号码导出vcf格式，号码去重工具，公开号码采集，号码对比工具，不同国家号码区分，批量添加国家代码，号码提取工具。"
        },
        {
          hid: 'description',
          name: 'description',
          content: "叮当助手（全球号）具有全球号码在线生成、对号码数据多样化处理、采集公开号码资源等强大功能，精准提升您的营销效率。"
        }
      ]
    }
  }
}
</script>
