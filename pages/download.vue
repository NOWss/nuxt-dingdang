<template>
  <div>
    <Header/>
    <DownloadUi/>
    <Footer/>
  </div>
</template>
<script>
import Header from "~/components/Header.vue";
import Footer from "~/components/Footer.vue";
import DownloadUi from "@/components/DownloadUi.vue";
import Strapi from 'strapi-sdk-javascript'

export default {
  name: "download",
  components: {
    Header,
    Footer,
    DownloadUi
  },
  head() {
    return {
      title: "叮当助手(全球号）|专业的多功能号码处理软件-dingdang",
      meta: [
        {
          hid: 'keywords',
          name: 'keywords',
          content: "手机号码处理软件，全球号码处理工具，海外号码生成器，随机号码生成器，号段生成器，vcf文件生成器，号码排序工具，号码乱序工具，号码去重工具，数据去重软件，手机号码采集软件，号码对比工具，批量添加国家代码工具。"
        },
        {
          hid: 'description',
          name: 'description',
          content: "叮当助手（全球号）具有全球号码在线生成、对号码数据多样化处理、采集公开号码资源等强大功能，精准提升您的营销效率。下载注册，即可免费使用多种号码处理功能，迅速提升业务效能！"
        }
      ]
    }
  }
}
</script>
<style scoped>

</style>
