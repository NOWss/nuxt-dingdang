<template>
  <section class="banner-two" id="banner">
    <span class="banner-two__shape-1"></span>
    <span class="banner-two__shape-2"></span>
    <span class="banner-two__shape-3"></span>
    <span class="banner-two__shape-4"></span>
    <div class="container" style="position: relative">
      <div class="banner-two__moc">
        <img src="/assets/images/mocs/banner-moc-2-1.png" alt="全球手机号码智能处理软件"/>
      </div>
      <div class="row">
        <div class="col-xl-6 col-lg-8">
          <div class="banner-two__content">
            <h1 class="banner-two__title">专业的号码处理软件</h1><!-- /.banner-two__title -->
            <h2 class="banner-two__subtitle">从号码生成、处理到精准触达<br/>营销效率提升<span>300%！</span></h2>
            <p class="banner-two__text">
              叮当助手(全球号)作为全球手机号码智能处理软件，软件具备提供全球精选号段实时更新、预测号码实号比例、全球号码在线自动生成、多样化的号码处理功能，更多个性化定制工具辅助使用。</p>
            <!-- /.banner-two__text -->
            <nuxt-link to="/download" class="banner-two__btn thm-btn "><span>下载应用</span></nuxt-link>
<!--            <p class="banner-two__text" style="font-size: 12px;">-->
<!--              立即下载，开启免费体验！注册即享免费使用号码处理功能，单次最大可导入40M大文件，轻松实现号码排序乱序、清除非手机号码、号码多样去重、双格式导出，叮当助手让号码处理变得简单高效！-->
<!--            </p>-->
            <!-- /.thm-btn -->
          </div><!-- /.banner-two__content -->
        </div><!-- /.col-lg-6 -->
      </div><!-- /.row -->
    </div><!-- /.container -->
  </section>
</template>

<script>
export default {
  name: "BannerTwo"
}
</script>

<style scoped lang="less">

</style>
