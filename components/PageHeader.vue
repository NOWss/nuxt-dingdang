<template>
  <section class="inner-banner">
    <span class="banner-two__shape-1"></span>
    <span class="banner-two__shape-2"></span>
    <span class="banner-two__shape-3"></span>
    <span class="banner-two__shape-4"></span>
    <div class="container">
      <ul class="list-unstyled thm-breadcrumb" style="padding-left: 0;">
        <li><a href="/">主页</a></li>
        <li class="active">{{ title}}</li>
      </ul><!-- /.list-unstyled -->
      <h1 class="inner-banner__title">{{ title}}</h1><!-- /.inner-banner__title -->
    </div><!-- /.container -->
  </section>
</template>

<script>
    export default {
      name: "PageHeader",
      props: {
        title: {
          type: String
        }
      }
    }
</script>

<style scoped>
</style>
