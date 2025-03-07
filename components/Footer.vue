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

      <div class="site-footer__upper">
        <div class="container">
          <div class="inner-container">
            <div class="row">
              <div class="col-lg-4">
                <div class="footer-widget">
                  <div>
                    <img src="/assets/images/resources/logo-dark.png" alt="logo" width="150" class="main-logo">
                  </div>
                  <nuxt-link class="download" to="/download">
                      <i class="iconfont icon-xiazai_xiazai"></i>
                      下载应用
                  </nuxt-link>
                </div>
              </div>
              <div class="col-lg-5">
                <div class="footer-widget">
                  <h3 class="footer-widget__title" style="font-size: 28px;">联系我们</h3>
                  <p>
                    <i class="fa fa-clock-o" aria-hidden="true"></i>
                    工作时间： 9:00AM-4:00AM
                  </p>
                  <p>
                    <i class="iconfont icon-telegram"></i>
                    联系客服： <a href="https://t.me/dingdangtw" target="_blank">@dingdangtw</a>
                  </p>
                  <p>
                    <i class="fa fa-globe" aria-hidden="true"></i>
                    资源入驻： <a href="https://t.me/tax678" target="_blank">@tax678</a>
                  </p>
                </div>
              </div>
              <div class="col-lg-3">
                <div class="footer-widget">
                  <h3 class="footer-widget__title" style="font-size: 28px;">Important</h3>
                  <p>
                    叮当助手仅支持美元付款，任何非美元收款的通道，可能存在诈骗风险，请注意辨别.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="site-footer__bottom">
        <div class="container">
          <div class="inner-container text-center">
            <p class="site-footer__copy">&copy; copyright 2024 by <a href="#">new.dingdang.tw</a></p>
            <!-- /.site-footer__copy -->
          </div><!-- /.inner-container -->
        </div><!-- /.container -->
      </div><!-- /.site-footer__bottom -->
    </footer>
    <a href="#" data-target="html" class="scroll-to-target scroll-to-top">
      <i class="iconfont icon-fanhuidingbu"></i>
    </a>
    <div class="sidebar-right">
      <div class="item" @click.stop="dialog = true">
        <i class="iconfont icon-comment"></i>
      </div>
      <nuxt-link class="item" to="/download">
        <i class="iconfont icon-xiazai_xiazai"></i>
      </nuxt-link>
      <a class="item" href="https://t.me/dingdangtw" target="_blank">
        <i class="iconfont icon-telegram"></i>
      </a>
    </div>
    <v-dialog v-model="dialog" persistent max-width="600px">
      <v-card>
        <v-card-title>
          <span class="text-h5">在线留言</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" sm="12" md="12">
                <v-textarea solo name="input-7-4" label="输入你想反馈的内容" v-model="submitData.content"></v-textarea>
              </v-col>
              <v-col cols="12" sm="12" md="12">
                <v-text-field label="联系人姓名" hint="此为必填项" v-model="submitData.name"></v-text-field>
              </v-col>
              <v-col cols="12" sm="12" md="12">
                <v-text-field label="手机号" persistent-hint required v-model="submitData.phone"></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field label="微信号" hint="此为必填项" required v-model="submitData.wechat"></v-text-field>
              </v-col>
            </v-row>
          </v-container>
          <small>*必填项请务必输入 否则无法提交！</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialog = false">
            取消
          </v-btn>
          <v-btn color="blue darken-1" text @click="submit">
            提交
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-snackbar v-model="snackbar.show" :color="snackbar.color" timeout="2000" top absolute :style="{ zIndex: 9999 }">
      {{ snackbar.text }}
      <template v-slot:action="{ attrs }">
        <v-btn color="blue" text v-bind="attrs" @click="snackbar.show = false">
          关闭
        </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<script>
export default {
  name: "Footer",
  data() {
    return {
      dialog: false,
      submitData: {
        content: "",
        name: "",
        phone: "",
        wechat: ""
      },
      snackbar: {
        show: false,
        color: 'success',
        text: ""
      }
    }
  },
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
  },
  methods: {
    showMessage(text, type = "success") {
      this.snackbar.text = text;
      this.snackbar.color = type === "error" ? "red" : "green";
      this.snackbar.show = true;
    },
    async submit() {
      const data = {
        data: {
          content: this.submitData.content,
          name: this.submitData.name,
          phone: this.submitData.phone,
          wechat: this.submitData.wechat
        }
      }
      try {
        if (this.submitData.name === "" && this.submitData.wechat === '') {
          this.showMessage('请务必填入必填项')
          return
        }
        const apiBase = this.$config.API_BASE;
        const res = await fetch(`${apiBase}/messages`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data)
        })
        this.showMessage('提交成功')
        this.dialog = false
      } catch (error) {
        console.error("创建失败", error);
      }
    }
  }
}
</script>

<style scoped>
.download {
  font-size: 18px;
  margin-top: 40px;
  background: #fff;
  box-shadow: 0 2px 8px rgba(28, 31, 35, .08), 0 16px 48px 8px rgba(28, 31, 35, .08);
  color: #000;
  border-radius: 30px;
  display: inline-block;
  padding: 10px 20px;
  cursor: pointer;

  i {
    font-size: 18px;
    color: #000;
  }

  &:hover{
    color: #FE6F9F;

    i{
      color: #FE6F9F;
    }
  }
}

.sidebar-right {
  position: fixed;
  right: 40px;
  bottom: 300px;
  width: 45px;
  height: 180px;
  z-index: 9999;
  border-radius: 20px 0 0 20px;
  background-size: 200% auto;
  display: flex;
  align-items: center;
  flex-wrap: wrap;

  .item {
    display: inline-block;
    width: 45px;
    height: 45px;
    background: #fff;
    text-align: center;
    -webkit-transition: .4s;
    transition: .4s;
    border-radius: 50%;
    box-shadow: 0 2px 8px rgba(28, 31, 35, .08), 0 16px 48px 8px rgba(28, 31, 35, .08);
    cursor: pointer;

    i {
      color: #000;
      font-size: 20px;
      font-weight: bold;
      line-height: 45px;
    }

    &:hover {
      i {
        color: #FE6F9F;
      }
    }
  }
}
</style>
