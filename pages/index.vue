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
      title: "叮当助手（全球号）|一站式号码数据生成与处理平台|海外号码生成器|手机号码处理软件-dingdang",
      meta: [
        {
          hid: 'keywords',
          name: 'keywords',
          content: "手机号码处理软件，全球号码处理工具，海外号码生成器，随机号码生成器，号段生成器，vcf文件生成器，号码排序工具，号码乱序工具，号码去重工具，数据去重软件，手机号码采集软件，号码对比工具，批量添加国家代码工具。"
        },
        {
          hid: 'description',
          name: 'description',
          content: "叮当助手(全球号）为您提供多个高效便捷的全球号码数据处理工具。您可以使用叮当助手(全球号）对号码数据进行大批量导入、排序乱序、清除非手机号码、号码对比去重、vcf格式导出、按需求筛选、批量添加区号、区分不同国家、智能识别提取等操作处理，并可在线批量生成全球号码、采集最新的公开号码数据，为您的业务发展降本提效。"
        }
      ]
    }
  }
}
</script>
