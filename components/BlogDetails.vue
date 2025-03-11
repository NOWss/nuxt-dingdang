<template>
  <section class="blog-details">
    <div class="container">
      <div class="row">
        <div class="col-lg-8">
          <div class="blog-one__single">
            <div class="blog-one__image">
              <!--              <img src="/assets/images/blog/blog-d-1-1.jpg" alt="">-->
              <img style="height: auto;" :src="`https://newcms.dingdang.tw${blog.ad.data.attributes.url}`"
                   :alt="blog.title">
            </div><!-- /.blog-one__image -->
            <div class="blog-one__content" style="padding: 0 50px;padding-top: 45px;padding-bottom: 40px;">
              <h2 class="blog-one__title">
                {{ blog.title }}
              </h2><!-- /.blog-one__title -->
              <ul class="list-unstyled blog-one__meta">
                <li>{{ blog.createdAt.split('T')[0] }}</li>
              </ul><!-- /.list-unstyled -->
              <div class="blog-one__text">
                <div class="blog_content" v-html="blog.content"></div>
              </div>
              <!-- /.blog-one__text -->
            </div><!-- /.blog-one__content -->
          </div><!-- /.blog-one__single -->
        </div><!-- /.col-lg-8 -->
        <div class="col-lg-4">
          <div class="sidebar">
            <!--            <div class="sidebar__single sidebar__search">-->
            <!--              <form action="#" class="sidebar__search-form">-->
            <!--                <input type="text" name="search" placeholder="Search here...">-->
            <!--                <button type="submit"><i class="fa fa-search"></i></button>-->
            <!--              </form>-->
            <!--            </div>&lt;!&ndash; /.sidebar__single &ndash;&gt;-->
            <div class="sidebar__single sidebar__post">
              <h3 class="sidebar__title">最新新闻</h3><!-- /.sidebar__title -->
              <div class="sidebar__post-wrap">
                <div class="sidebar__post__single" v-for="item in newBlogs.data">
                  <div class="sidebar__post-image">
                    <div class="inner-block">
                      <img :src="`https://newcms.dingdang.tw${item.attributes.ad.data.attributes.url}`"
                           :alt="item.attributes.title">
                    </div>
                    <!-- /.inner-block -->
                  </div><!-- /.sidebar__post-image -->
                  <div class="sidebar__post-content">
                    <h4 class="sidebar__post-title" :title="item.attributes.title">
                      <nuxt-link :to="`/blog-details/${item.attributes.slug}`">{{ item.attributes.title }}</nuxt-link>
                    </h4>
                    <!-- /.sidebar__post-title -->
                  </div><!-- /.sidebar__post-content -->
                </div><!-- /.sidebar__post__single -->
              </div><!-- /.sidebar__post-wrap -->
            </div><!-- /.sidebar__single -->
            <div class="sidebar__single sidebar__tags">
              <h3 class="sidebar__title">Tags</h3><!-- /.sidebar__title -->
              <ul class="sidebar__tags-list">
                <li class="sidebar__tags-list-item" v-for="item in blog.tags.data">
                  <nuxt-link :to="`/blog?tag=${item.attributes.tag_name}`">{{ item.attributes.tag_name }}</nuxt-link>
                </li>
              </ul><!-- /.sidebar__category-list -->
            </div><!-- /.sidebar__single -->
          </div><!-- /.sidebar -->
        </div><!-- /.col-lg-4 -->
      </div><!-- /.row -->
    </div><!-- /.container -->
  </section>
</template>

<script>
import Strapi from "strapi-sdk-javascript";

export default {
  name: "BlogDetails",
  props: {
    blog: {  // 定义接收 blogs 的 props
      type: Object,
      required: true
    },
    newBlogs: {
      type: Object,
      required: true
    }
  },
  mounted() {
    window.onload = function () {
      // 获取文章内容容器
      const detailsContent = document.querySelector('.blog-details .blog-one__text .blog_content');

      // 获取容器内的所有 <a> 标签
      const links = detailsContent.getElementsByTagName('a');

      // 遍历所有 <a> 标签，设置 target="_blank"
      for (let i = 0; i < links.length; i++) {
        links[i].setAttribute('target', '_blank');
      }
    }
  },
  head() {
    return {
      title: this.blog.title + '-dingdang',
      meta: [
        {
          hid: 'keywords',
          name: 'keywords',
          content: this.blog.keywords
        },
        {
          hid: 'description',
          name: 'description',
          content: this.blog.description
        }
      ]
    }
  }
}
</script>

<style scoped>

</style>
