<template>
  <div>
    <HeaderThree/>
    <Check/>
    <Footer/>
  </div>
</template>
<script>
import HeaderThree from "~/components/HeaderThree.vue";
import Footer from "~/components/Footer.vue";
import Check from "@/components/Check.vue";

export default {
  name: 'check',
  components: {
    HeaderThree,
    Footer,
    Check
  },
  head() {
    return {
      title: "官方防伪查询-叮当助手（全球号）-dingdang",
      meta: [
        {
          hid: 'keywords',
          name: 'keywords',
          content: "手机号码处理软件，全球号码处理工具，海外号码生成器，随机号码生成器，号段生成器，vcf文件生成器，号码排序工具，号码乱序工具，号码去重工具，数据去重软件，手机号码采集软件，号码对比工具，批量添加国家代码工具。"
        },
        {
          hid: 'description',
          name: 'description',
          content: "叮当助手（全球号）具有大批量号码数据秒级导入、手机号码排序乱序、清除非手机号码数据、号码对比与去重、vcf格式导出、批量添加区号、区分不同国家号码、提取号码数据等强大的号码处理功能，并可以为您生成全球任意国家地区的号码数据，全球公开号码数据供您下载使用，助您提升号码处理效率。"
        }
      ]
    }
  }
}
</script>
<style scoped>

</style>
