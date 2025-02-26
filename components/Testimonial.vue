<template>
  <section class="testimonials-one">
    <div class="container">
      <div class="block-title text-center">
        <h2 class="block-title__title">客户评价</h2><!-- /.block-title__title -->
      </div><!-- /.block-title -->
      <div class="testimonials-one__carousel-outer">
        <div class="testimonials-one__carousel owl-carousel owl-theme">
          <div class="item">
            <div class="testimonials-one__single">
              <div class="testimonials-one__inner">
                <p>作为跨境行业的运营人员，叮当助手的号码处理功能非常全面，尤其是大批量导入导出和去重功能，极大提升了我们处理客户订单的效率。自定义筛选和排序乱序功能也非常灵活，帮助我们精准定位目标客户。</p>
                <h3>Shirley Smith</h3>
                <span>我们的客户</span>
                <img src="/assets/images/resources/testi-1-1.png" alt="Awesome Image" />
              </div><!-- /.testimonials-one__inner -->
            </div><!-- /.testimonials-one__single -->
          </div><!-- /.item -->
          <div class="item">
            <div class="testimonials-one__single">
              <div class="testimonials-one__inner">
                <p>作为国际物流行业的调度负责人，导出功能非常便捷，支持多种格式，txt和vcf格式的导出，方便我们与其他系统或设备进行数据对接，提升了客户信息管理的效率。</p>
                <h3>Shirley Smith</h3>
                <span>我们的客户</span>
                <img src="/assets/images/resources/testi-1-1.png" alt="Awesome Image" />
              </div><!-- /.testimonials-one__inner -->
            </div><!-- /.testimonials-one__single -->
          </div><!-- /.item -->
          <div class="item">
            <div class="testimonials-one__single">
              <div class="testimonials-one__inner">
                <p>使用叮当助手后，我明显感觉到成本得到了有效控制，尤其是在时间和资源上的节省，让我能够更专注于核心业务。
                  叮当助手彻底改变了我的工作流程，其高效的功能让我在短时间内完成了大量任务，真正实现了效率的飞跃。</p>
                <h3>Shirley Smith</h3>
                <span>我们的客户</span>
                <img src="/assets/images/resources/testi-1-1.png" alt="Awesome Image" />
              </div><!-- /.testimonials-one__inner -->
            </div><!-- /.testimonials-one__single -->
          </div><!-- /.item -->
          <div class="item">
            <div class="testimonials-one__single">
              <div class="testimonials-one__inner">
                <p>一站式操作让我无需切换多个平台，所有需求都能在一个APP内完成，极大地简化了我的工作流程。</p>
                <h3>Shirley Smith</h3>
                <span>我们的客户</span>
                <img src="/assets/images/resources/testi-1-1.png" alt="Awesome Image" />
              </div><!-- /.testimonials-one__inner -->
            </div><!-- /.testimonials-one__single -->
          </div><!-- /.item -->
          <div class="item">
            <div class="testimonials-one__single">
              <div class="testimonials-one__inner">
                <p>叮当助手的用户界面设计得非常直观，即使是初次使用也能快速上手，极大地降低了学习成本。</p>
                <h3>Shirley Smith</h3>
                <span>我们的客户</span>
                <img src="/assets/images/resources/testi-1-1.png" alt="Awesome Image" />
              </div><!-- /.testimonials-one__inner -->
            </div><!-- /.testimonials-one__single -->
          </div><!-- /.item -->
          <div class="item">
            <div class="testimonials-one__single">
              <div class="testimonials-one__inner">
                <p>叮当助手的号码处理功能非常专业，尤其是去重和过滤无效号码的操作，让我们的数据质量大幅提升。导出格式也很灵活，直接对接我们的CRM系统，省去了很多麻烦。</p>
                <h3>Shirley Smith</h3>
                <span>我们的客户</span>
                <img src="/assets/images/resources/testi-1-1.png" alt="Awesome Image" />
              </div><!-- /.testimonials-one__inner -->
            </div><!-- /.testimonials-one__single -->
          </div><!-- /.item -->
          <div class="item">
            <div class="testimonials-one__single">
              <div class="testimonials-one__inner">
                <p>作为一家中小企业，我们预算有限，但叮当助手的性价比真的很高！不仅提高了数据质量，团队协作也更顺畅。叮当助手让我们的业务更上一层楼。</p>
                <h3>Shirley Smith</h3>
                <span>我们的客户</span>
                <img src="/assets/images/resources/testi-1-1.png" alt="Awesome Image" />
              </div><!-- /.testimonials-one__inner -->
            </div><!-- /.testimonials-one__single -->
          </div><!-- /.item -->
        </div><!-- /.testimonials-one__carousel -->
        <div class="testimonials-one__carousel__shape-one"></div><!-- /.testimonials-one__carousel__shape-one -->
        <div class="testimonials-one__carousel__shape-two"></div><!-- /.testimonials-one__carousel__shape-two -->
        <div class="testimonials-one__nav">
          <a class="testimonials-one__nav-left" href="#"><i class="dimon-icon-left-arrow"></i></a>
          <a class="testimonials-one__nav-right" href="#"><i class="dimon-icon-right-arrow"></i></a>
        </div><!-- /.testimonials-one__nav -->
      </div><!-- /.testimonials-one__carousel-outer -->
    </div><!-- /.container -->
  </section>
</template>

<script>
    export default {
      name: "Testimonial",
      mounted() {
        if ($('.testimonials-one__carousel').length) {
          $('.testimonials-one__carousel').owlCarousel({
            loop: true,
            margin: 0,
            nav: false,
            dots: false,
            autoWidth: false,
            autoplay: true,
            smartSpeed: 700,
            autoplayTimeout: 5000,
            autoplayHoverPause: true,
            items: 1
          });

          $('.testimonials-one__nav-left').on('click', function() {
            $('.testimonials-one__carousel').trigger('next.owl.carousel');
            return false;
          });
          $('.testimonials-one__nav-right').on('click', function() {
            $('.testimonials-one__carousel').trigger('prev.owl.carousel');
            return false;
          });
        }
      }
    }
</script>

<style scoped>

</style>
