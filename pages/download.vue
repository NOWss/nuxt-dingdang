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
  }
}
</script>
<style scoped>

</style>
