<template>
  <div>
    <HeaderThree/>
    <AreaSearch :areas="areas" />
    <Footer/>
  </div>
</template>
<script>
import Footer from "@/components/Footer.vue";
import HeaderThree from "@/components/HeaderThree.vue";
import AreaSearch from "~/components/AreaSearch.vue";
import Strapi from "strapi-sdk-javascript";
export default {
  name:'areaCode',
  components: {HeaderThree, Footer,AreaSearch},
  async asyncData({$config,error}){
    try{
      let areas
      const apiBase = $config.API_BASE;
      const collection = 'areas';
      let apiUrl, queryParams;
      apiUrl = `${apiBase}/${collection}`;
      queryParams = {
        'filters[type][$eq]': 'countrys'
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
      areas = dataRaw;
      if (!areas) {
        console.error(`找不到匹配的数据`);
        error({statusCode: 404, message: '无法找到这篇内容'});
        return; // 提前终止
      }
      return {areas: areas.data};
    }
    catch (err) {
      console.error('Strapi API 请求失败:', err);
    }
  },
  head() {
    return {
      title: "全球地区代码查询-叮当助手（全球号）-dingdang",
      meta: [
        {
          hid: 'keywords',
          name: 'keywords',
          content: "全球国家代码查询，地区代码查询，国家地区代码查询。"
        },
        {
          hid: 'description',
          name: 'description',
          content: "叮当助手（全球号）为您提供免费、精准、便捷的全球地区代码查询服务，助您轻松获取全球国家任意地区的地区代码信息。"
        }
      ]
    }
  }
}
</script>

<style scoped>

</style>
