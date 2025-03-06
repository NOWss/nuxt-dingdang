<template>
  <v-app>
    <div class="page-wrapper">
      <Preloader/>
      <nuxt/>
    </div>
  </v-app>
</template>


<script>
import Preloader from "~/components/Preloader.vue";

export default {
  components: {
    Preloader
  },
  head() {
    return {
      title: "Dimon | Vue Nuxt Software App Landing Page Template"
    }
  }

}
</script>
