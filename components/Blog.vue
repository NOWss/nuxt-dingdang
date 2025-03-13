<template>
  <section class="blog-one">
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-md-6 col-sm-12 wow fadeInUp" v-for="blog in blogs.data" :key="blog.id">
          <div class="blog-one__single">
            <div class="blog-one__image">
              <img :src="`https://newcms.dingdang.tw${blog.attributes.ad.data.attributes.url}`" alt="">
              <nuxt-link class="blog-one__more-link" :to="`/blog-details/${blog.attributes.slug}`"><i
                class="fa fa-link"></i>
                <!-- /.fa fa-link --></nuxt-link>
            </div><!-- /.blog-one__image -->
            <div class="blog-one__content">
              <ul class="list-unstyled blog-one__meta">
                <li>
                  <nuxt-link :to="`/blog-details/${blog.attributes.slug}`">
                    {{ blog.attributes.createdAt.split('T')[0] }}
                  </nuxt-link>
                </li>
              </ul><!-- /.list-unstyled -->
              <h3 class="blog-one__title">
                <nuxt-link :to="`/blog-details/${blog.attributes.slug}`" :title="blog.attributes.title">
                  {{ blog.attributes.title }}
                </nuxt-link>
              </h3><!-- /.blog-one__title -->
              <nuxt-link :to="`/blog-details/${blog.attributes.slug}`" class="blog-one__link">了解更多</nuxt-link>
              <!-- /.blog-one__link -->
            </div><!-- /.blog-one__content -->
          </div><!-- /.blog-one__single -->
        </div><!-- /.col-lg-4 -->
      </div><!-- /.row -->
      <pagination :current-page="blogs.meta.pagination.page" :total-items="blogs.meta.pagination.total"
                  :items-per-page="blogs.meta.pagination.pageSize"/>
    </div><!-- /.container -->
  </section>
</template>

<script>
import pagination from './pagination.vue'

export default {
  name: "Blog",
  components: {
    pagination
  },
  props: {
    blogs: {  // 定义接收 blogs 的 props
      type: Object,
      required: true
    },
    pageCount: {
      type: Number,
      required: true
    }
  },
  mounted() {
    console.log(this.blogs)
  },
}
</script>

<style scoped>

</style>
