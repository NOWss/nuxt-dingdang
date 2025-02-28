<template>
  <div>
    <footer class="site-footer">
      <!--      <div class="site-footer__upper">-->
      <!--        <div class="container">-->
      <!--          <div class="row">-->
      <!--            <div class="col-lg-3">-->
      <!--              <div class="footer-widget footer-widget__about">-->
      <!--                <img src="/assets/images/resources/logo-dark.png" width="119" alt="" class="footer-widget__logo">-->
      <!--                <p class="footer-widget__contact"><a href="tel:888-666-0000">888 666 0000</a></p>-->
      <!--                &lt;!&ndash; /.footer-widget__contact &ndash;&gt;-->
      <!--                <p class="footer-widget__contact"><a href="mailto:needhelp@example.com">needhelp@example.com</a>-->
      <!--                <p class="footer-widget__contact">855 road, broklyn street <br> new york 600</p>&lt;!&ndash; /.footer-widget__contact &ndash;&gt;-->
      <!--              </div>&lt;!&ndash; /.footer-widget &ndash;&gt;-->
      <!--            </div>&lt;!&ndash; /.col-lg-2 &ndash;&gt;-->
      <!--            <div class="col-lg-6 d-flex justify-content-between footer-widget__links-wrap">-->
      <!--              <div class="footer-widget">-->
      <!--                <h3 class="footer-widget__title">Explore</h3>&lt;!&ndash; /.footer-widget__title &ndash;&gt;-->
      <!--                <ul class="footer-widget__links list-unstyled">-->
      <!--                  <li><a href="#">About</a></li>-->
      <!--                  <li><a href="#">Our Team</a></li>-->
      <!--                  <li><a href="#">Features</a></li>-->
      <!--                  <li><a href="#">Blog</a></li>-->
      <!--                  <li><a href="#">How It Works</a></li>-->
      <!--                </ul>&lt;!&ndash; /.footer-widget__links &ndash;&gt;-->
      <!--              </div>&lt;!&ndash; /.footer-widget &ndash;&gt;-->
      <!--              <div class="footer-widget">-->
      <!--                <h3 class="footer-widget__title">Services</h3>&lt;!&ndash; /.footer-widget__title &ndash;&gt;-->
      <!--                <ul class="footer-widget__links list-unstyled">-->
      <!--                  <li><a href="#">Speed Optimization </a></li>-->
      <!--                  <li><a href="#">Marketing Analysis </a></li>-->
      <!--                  <li><a href="#">SEO and Backlinks </a></li>-->
      <!--                  <li><a href="#">Content Marketing</a></li>-->
      <!--                </ul>&lt;!&ndash; /.footer-widget__links &ndash;&gt;-->
      <!--              </div>&lt;!&ndash; /.footer-widget &ndash;&gt;-->
      <!--              <div class="footer-widget">-->
      <!--                <h3 class="footer-widget__title">Links</h3>&lt;!&ndash; /.footer-widget__title &ndash;&gt;-->
      <!--                <ul class="footer-widget__links list-unstyled">-->
      <!--                  <li><a href="#">Help </a></li>-->
      <!--                  <li><a href="#">Support </a></li>-->
      <!--                  <li><a href="#">Clients </a></li>-->
      <!--                  <li><a href="#">Contact</a></li>-->
      <!--                </ul>&lt;!&ndash; /.footer-widget__links &ndash;&gt;-->
      <!--              </div>&lt;!&ndash; /.footer-widget &ndash;&gt;-->
      <!--            </div>&lt;!&ndash; /.col-lg-6 &ndash;&gt;-->
      <!--            <div class="col-lg-3">-->
      <!--              <div class="footer-widget">-->
      <!--                <div class="site-footer__social">-->
      <!--                  <a href="#" class="fa fa-facebook-square"></a>-->
      <!--                  <a href="#" class="fa fa-twitter"></a>-->
      <!--                  <a href="#" class="fa fa-instagram"></a>-->
      <!--                  <a href="#" class="fa fa-pinterest-p"></a>-->
      <!--                </div>&lt;!&ndash; /.site-footer__social &ndash;&gt;-->
      <!--              </div>&lt;!&ndash; /.footer-widget &ndash;&gt;-->
      <!--            </div>&lt;!&ndash; /.col-lg-4 &ndash;&gt;-->
      <!--          </div>&lt;!&ndash; /.row &ndash;&gt;-->
      <!--        </div>&lt;!&ndash; /.container &ndash;&gt;-->
      <!--      </div>&lt;!&ndash; /.site-footer__upper &ndash;&gt;-->
      <div class="site-footer__bottom">
        <div class="container">
          <div class="inner-container text-center">
            <p class="site-footer__copy">&copy; copyright 2024 by <a href="#">Layerdrops.com</a></p>
            <!-- /.site-footer__copy -->
          </div><!-- /.inner-container -->
        </div><!-- /.container -->
      </div><!-- /.site-footer__bottom -->
    </footer>
    <a href="#" data-target="html" class="scroll-to-target scroll-to-top"><i class="fa fa-angle-up"></i></a>

<!--    <div class="sidebar-right">-->
<!--      <a class="item">-->
<!--        <span>-->
<!--          <i class="fa fa-telegram"></i>-->
<!--          客服-->
<!--        </span>-->
<!--      </a>-->
<!--      <a class="item">-->
<!--        <span>-->
<!--          <i class="fa fa-telegram"></i>-->
<!--          客服-->
<!--        </span>-->
<!--      </a>-->
<!--      <a class="item">-->
<!--        <span>-->
<!--          <i class="fa fa-telegram"></i>-->
<!--          客服-->
<!--        </span>-->
<!--      </a>-->
<!--    </div>-->
  </div>
</template>

<script>
export default {
  name: "Footer",
  mounted() {

    $(window).on('scroll', function () {
      if ($('.scroll-to-top').length) {
        var strickyScrollPos = 100;
        if ($(window).scrollTop() > strickyScrollPos) {
          $('.scroll-to-top').fadeIn(500);
        } else if ($(this).scrollTop() <= strickyScrollPos) {
          $('.scroll-to-top').fadeOut(500);
        }
      }
    })
  }
}
</script>

<style scoped>
.sidebar-right {
  position: fixed;
  right: 0px;
  bottom: 400px;
  width: 70px;
  height: 250px;
  z-index: 9999;
  border-radius: 20px 0 0 20px;
  background-image: -webkit-gradient(linear, left top, right top, from(#ff4eb5), color-stop(51%, #ffa065), to(#ff4eb5));
  background-image: linear-gradient(to right, #ff4eb5 0%, #ffa065 51%, #ff4eb5 100%);
  background-size: 200% auto;
  display: flex;
  align-items: center;
  flex-wrap: wrap;

  .item{
    width: 100%;
    padding: 20px;
    text-align: center;
    box-sizing: border-box;
    height: 33.3%;

    span{
      color: #fff;
      font-size: 14px;
      display: flex;
      flex-wrap: wrap;
      justify-content: center;

      *{
        width: 100%;
      }
      i{
        font-size: 24px;
      }
    }
  }
}
</style>
