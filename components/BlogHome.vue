<template>
  <section class="blog-one blog-one__home thm-gray-bg" id="news">
    <div class="container">
      <div class="block-title text-center">
        <h2 class="block-title__title">Checkout Our <span>Latest</span> <br> News & Articles.</h2><!-- /.block-title__title -->
      </div><!-- /.block-title -->
      <div class="row">
        <div class="col-lg-4 col-md-12 col-sm-12 wow fadeInUp" data-wow-duration="1500ms" v-for="blog in blogs" :key="blog.id">
          <div class="blog-one__single">
            <div class="blog-one__image">
              <img src="/assets/images/blog/blog-1-1.jpg" alt="">
              <a class="blog-one__more-link" href="news-details.html"><i class="fa fa-link"></i>
                <!-- /.fa fa-link --></a>
            </div><!-- /.blog-one__image -->
            <div class="blog-one__content">
              <ul class="list-unstyled blog-one__meta">
                <li><a href="#">{{ blog.attributes.createdAt.split('T')[0] }}</a></li>
<!--                <li><a href="#">2 Comments</a></li>-->
              </ul><!-- /.list-unstyled -->
              <h3 class="blog-one__title" :title="blog.attributes.title">
                <nuxt-link to="/blog-details">{{ blog.attributes.title }}</nuxt-link>
              </h3><!-- /.blog-one__title -->
              <nuxt-link to="/blog-details" class="blog-one__link">了解更多</nuxt-link><!-- /.blog-one__link -->
            </div><!-- /.blog-one__content -->
          </div><!-- /.blog-one__single -->
        </div ><!-- /.col-lg-4 -->
      </div><!-- /.row -->
    </div><!-- /.container -->
  </section>
</template>

<script>
    export default {
      name: "BlogHome",
      props: {
        blogs: {  // 定义接收 blogs 的 props
          type: Array,
          required: true
        }
      }
    }
</script>

<style scoped>

</style>
