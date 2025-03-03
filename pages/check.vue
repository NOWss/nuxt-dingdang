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
  }
}
</script>
<style scoped>

</style>
