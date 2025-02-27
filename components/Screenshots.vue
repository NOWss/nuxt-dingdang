<template>
  <section class="app-shot-one" id="screenshots">
    <img src="/assets/images/background/app-shot-bg.png" alt="Awesome Image" class="app-shot-one__bg"/>
    <div class="container-fluid">
      <div class="block-title text-center">
        <h2 class="block-title__title">叮当助手<span>精选号段</span><br/>操作流程</h2><!-- /.block-title__title -->
      </div><!-- /.block-title -->
      <div class="app-shot-one__carousel owl-theme owl-carousel">
        <div class="item">
          <img src="/assets/images/jxhd/1.png" alt="">
        </div><!-- /.item -->
        <div class="item">
          <img src="/assets/images/jxhd/2.png" alt="">
        </div><!-- /.item -->
        <div class="item">
          <img src="/assets/images/jxhd/3.png" alt="">
        </div><!-- /.item -->
        <div class="item">
          <img src="/assets/images/jxhd/4.png" alt="">
        </div><!-- /.item -->
      </div><!-- /.app-shot-one__carousel owl-theme owl-carousel -->
    </div><!-- /.container-fluid -->
  </section>
</template>

<script>
export default {
  name: "Screenshots",
  mounted() {

    if ($('.app-shot-one__carousel').length) {
      $('.app-shot-one__carousel').owlCarousel({
        loop: true,
        margin: 43,
        nav: false,
        dots: false,
        autoWidth: false,
        autoplay: true,
        smartSpeed: 700,
        autoplayTimeout: 5000,
        autoplayHoverPause: true,
        slideBy: 5,
        responsive: {
          0: {items: 1},
          1280: {items: 3},
          1680: {items: 3},
        }
      });
    }
  }
}
</script>

<style scoped>

</style>
