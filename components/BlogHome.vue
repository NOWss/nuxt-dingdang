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
              <h3 class="blog-one__title">
                <nuxt-link to="/blog-details">{{ blog.attributes.title }}</nuxt-link>
              </h3><!-- /.blog-one__title -->
              <nuxt-link to="/blog-details" class="blog-one__link">了解更多</nuxt-link><!-- /.blog-one__link -->
            </div><!-- /.blog-one__content -->
          </div><!-- /.blog-one__single -->
        </div ><!-- /.col-lg-4 -->
<!--        <div class="col-lg-4 col-md-12 col-sm-12 wow fadeInDown" data-wow-duration="1500ms">-->
<!--          <div class="blog-one__single">-->
<!--            <div class="blog-one__image">-->
<!--              <img src="/assets/images/blog/blog-1-2.jpg" alt="">-->
<!--              <a class="blog-one__more-link" href="news-details.html"><i class="fa fa-link"></i>-->
<!--                &lt;!&ndash; /.fa fa-link &ndash;&gt;</a>-->
<!--            </div>&lt;!&ndash; /.blog-one__image &ndash;&gt;-->
<!--            <div class="blog-one__content">-->
<!--              <ul class="list-unstyled blog-one__meta">-->
<!--                <li><a href="#">22 Oct, 2019</a></li>-->
<!--                <li><a href="#">2 Comments</a></li>-->
<!--              </ul>&lt;!&ndash; /.list-unstyled &ndash;&gt;-->
<!--              <h3 class="blog-one__title">-->
<!--                <nuxt-link to="/blog-details">It is all exactly as i said, but i don't like it let's unpack-->
<!--                  that</nuxt-link>-->
<!--              </h3>&lt;!&ndash; /.blog-one__title &ndash;&gt;-->
<!--              <nuxt-link to="/blog-details" class="blog-one__link">Read More</nuxt-link>&lt;!&ndash; /.blog-one__link &ndash;&gt;-->
<!--            </div>&lt;!&ndash; /.blog-one__content &ndash;&gt;-->
<!--          </div>&lt;!&ndash; /.blog-one__single &ndash;&gt;-->
<!--        </div>&lt;!&ndash; /.col-lg-4 &ndash;&gt;-->
<!--        <div class="col-lg-4 col-md-12 col-sm-12 wow fadeInUp" data-wow-duration="1500ms">-->
<!--          <div class="blog-one__single">-->
<!--            <div class="blog-one__image">-->
<!--              <img src="/assets/images/blog/blog-1-3.jpg" alt="">-->
<!--              <a class="blog-one__more-link" href="news-details.html"><i class="fa fa-link"></i>-->
<!--                &lt;!&ndash; /.fa fa-link &ndash;&gt;</a>-->
<!--            </div>&lt;!&ndash; /.blog-one__image &ndash;&gt;-->
<!--            <div class="blog-one__content">-->
<!--              <ul class="list-unstyled blog-one__meta">-->
<!--                <li><a href="#">22 Oct, 2019</a></li>-->
<!--                <li><a href="#">2 Comments</a></li>-->
<!--              </ul>&lt;!&ndash; /.list-unstyled &ndash;&gt;-->
<!--              <h3 class="blog-one__title">-->
<!--                <nuxt-link to="/blog-details">I just wanted to give you a heads-up, or this you feel you-->
<!--                  would</nuxt-link>-->
<!--              </h3>&lt;!&ndash; /.blog-one__title &ndash;&gt;-->
<!--              <nuxt-link to="/blog-details" class="blog-one__link">Read More</nuxt-link>&lt;!&ndash; /.blog-one__link &ndash;&gt;-->
<!--            </div>&lt;!&ndash; /.blog-one__content &ndash;&gt;-->
<!--          </div>&lt;!&ndash; /.blog-one__single &ndash;&gt;-->
<!--        </div>&lt;!&ndash; /.col-lg-4 &ndash;&gt;-->
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
