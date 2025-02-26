<template>
  <section class="blog-details">
    <div class="container">
      <div class="row">
        <div class="col-lg-8">
          <div class="blog-one__single">
            <div class="blog-one__image">
              <img src="/assets/images/blog/blog-d-1-1.jpg" alt="">
<!--              <img :src="blog.ad.data.attributes.url" alt="">-->
            </div><!-- /.blog-one__image -->
            <div class="blog-one__content">
              <h2 class="blog-one__title">
                {{ blog.title }}
              </h2><!-- /.blog-one__title -->
              <ul class="list-unstyled blog-one__meta">
                <li>{{ blog.createdAt.split('T')[0]}}</li>
              </ul><!-- /.list-unstyled -->
              <div class="blog-one__text">
                <div v-html="blog.content"></div>
              </div>
              <!-- /.blog-one__text -->
            </div><!-- /.blog-one__content -->
          </div><!-- /.blog-one__single -->
        </div><!-- /.col-lg-8 -->
        <div class="col-lg-4">
          <div class="sidebar">
            <div class="sidebar__single sidebar__search">
              <form action="#" class="sidebar__search-form">
                <input type="text" name="search" placeholder="Search here...">
                <button type="submit"><i class="fa fa-search"></i></button>
              </form>
            </div><!-- /.sidebar__single -->
            <div class="sidebar__single sidebar__post">
              <h3 class="sidebar__title">最新新闻</h3><!-- /.sidebar__title -->
              <div class="sidebar__post-wrap">
                <div class="sidebar__post__single">
                  <div class="sidebar__post-image">
                    <div class="inner-block"><img src="/assets/images/blog/lp-1-1.jpg" alt="Awesome Image"></div>
                    <!-- /.inner-block -->
                  </div><!-- /.sidebar__post-image -->
                  <div class="sidebar__post-content">
                    <h4 class="sidebar__post-title"><a href="#">Pre launch mobile app marketing pitfalls</a></h4>
                    <!-- /.sidebar__post-title -->
                  </div><!-- /.sidebar__post-content -->
                </div><!-- /.sidebar__post__single -->
                <div class="sidebar__post__single">
                  <div class="sidebar__post-image">
                    <div class="inner-block"><img src="/assets/images/blog/lp-1-2.jpg" alt="Awesome Image"></div>
                    <!-- /.inner-block -->
                  </div><!-- /.sidebar__post-image -->
                  <div class="sidebar__post-content">
                    <h4 class="sidebar__post-title"><a href="#">Social currency per- formance keywords or</a></h4>
                    <!-- /.sidebar__post-title -->
                  </div><!-- /.sidebar__post-content -->
                </div><!-- /.sidebar__post__single -->
                <div class="sidebar__post__single">
                  <div class="sidebar__post-image">
                    <div class="inner-block"><img src="/assets/images/blog/lp-1-3.jpg" alt="Awesome Image"></div>
                    <!-- /.inner-block -->
                  </div><!-- /.sidebar__post-image -->
                  <div class="sidebar__post-content">
                    <h4 class="sidebar__post-title"><a href="#">Prioritize these items quarterly sales are at</a></h4>
                    <!-- /.sidebar__post-title -->
                  </div><!-- /.sidebar__post-content -->
                </div><!-- /.sidebar__post__single -->
              </div><!-- /.sidebar__post-wrap -->
            </div><!-- /.sidebar__single -->
            <div class="sidebar__single sidebar__tags">
              <h3 class="sidebar__title">Tags</h3><!-- /.sidebar__title -->
              <ul class="sidebar__tags-list">
                <li class="sidebar__tags-list-item"><a href="#">Business,</a></li>
                <li class="sidebar__tags-list-item"><a href="#">Agency,</a></li>
                <li class="sidebar__tags-list-item"><a href="#">Technology,</a></li>
                <li class="sidebar__tags-list-item"><a href="#">Parallax,</a></li>
                <li class="sidebar__tags-list-item"><a href="#">Innovative,</a></li>
                <li class="sidebar__tags-list-item"><a href="#">Professional,</a></li>
                <li class="sidebar__tags-list-item"><a href="#">Experience,</a></li>
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
    }
  },
  mounted() {
    console.log(this.blog)
  },
  head(){
    return{
      title: this.blog.title + '-dingdang',
      meta:[
        {
          hid:'keywords',
          name:'keywords',
          content:this.blog.keywords
        },
        {
          hid:'description',
          name:'description',
          content:this.blog.description
        }
      ]
    }
  }
}
</script>

<style scoped>

</style>
