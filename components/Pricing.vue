<template>
  <section class="pricing-one" id="pricing">
    <div class="container">
      <div class="block-title text-center">
        <h2 class="block-title__title">适合您的多种价格需求</h2><!-- /.block-title__title -->
      </div><!-- /.block-title -->
      <!--      <ul class="list-inline text-center switch-toggler-list" role="tablist" id="switch-toggle-tab">-->
      <!--        <li class="month active"><a href="#">Monthly</a></li>-->
      <!--        <li>-->
      <!--          &lt;!&ndash; Rounded switch &ndash;&gt;-->
      <!--          <label class="switch on">-->
      <!--            <span class="slider round"></span>-->
      <!--          </label>-->
      <!--        </li>-->
      <!--        <li class="year"><a href="#">Yearly</a></li>-->
      <!--      </ul>&lt;!&ndash; /.list-inline &ndash;&gt;-->
      <div class="tabed-content">
        <div id="month">
          <div class="row pricing-one__price-row">
            <div class="col-lg-3 wow fadeInUp" data-wow-duration="1500ms">
              <div class="pricing-one__single text-center">
                <h3>$0.00</h3>
                <p>叮当用户</p>
                <ul class="list-unstyled">
                  <li>手机号码排序乱序</li>
                  <li>清除非手机号码格式数据</li>
                  <li>号码数据去重</li>
                  <li>支持txt/vcf格式导出</li>
                  <li>按号段筛选号码</li>
                  <li>按数字组合特征筛选号码</li>
                  <li>单次最大支持40M文件导入</li>
                </ul><!-- /.list-unstyled -->
                <nuxt-link to="/download" class="thm-btn pricing-one__btn"><span>下载使用</span></nuxt-link>
                <span class="tag-line">注册即可使用!</span>
              </div><!-- /.pricing-one__single -->
            </div>
            <div class="col-lg-3 wow fadeInUp" data-wow-duration="1500ms">
              <div class="pricing-one__single text-center">
                <h3>$30.00</h3>
                <p>VIP月度会员</p>
                <ul class="list-unstyled">
                  <li>解锁全部高级功能</li>
                  <li>极速批量化处理</li>
                  <li>单次最大支持4G文件导入</li>
                  <li>客服7×24小时紧急支持</li>
                  <li>新功能首发体验资格</li>
                  <li>订阅即赠10天有效期</li>
                </ul><!-- /.list-unstyled -->
                <a href="https://t.me/dingdangtw" target="_blank" class="thm-btn pricing-one__btn"><span>前往充值</span></a>
                <span class="tag-line">应用内支持自动充值</span>
              </div><!-- /.pricing-one__single -->
            </div><!-- /.col-lg-4 -->
            <div class="col-lg-3 wow fadeInDown" data-wow-duration="1500ms">
              <div class="pricing-one__single text-center">
                <h3>$72.00</h3>
                <p>VIP季度会员</p>
                <ul class="list-unstyled">
                  <li>尊享8折超值优惠</li>
                  <li>极速批量化操作</li>
                  <li>单次最大支持4G文件导入</li>
                  <li>客服7×24小时紧急支持</li>
                  <li>新功能首发体验资格</li>
                  <li>超值省$18，成本直降</li>
                  <li>订阅即赠20天有效期</li>
                </ul><!-- /.list-unstyled -->
                <a href="https://t.me/dingdangtw" target="_blank" class="thm-btn pricing-one__btn"><span>前往充值</span></a>
                <span class="tag-line">应用内支持自动充值</span>
              </div><!-- /.pricing-one__single -->
            </div><!-- /.col-lg-4 -->
            <div class="col-lg-3 wow fadeInUp" data-wow-duration="1500ms">
              <div class="pricing-one__single text-center">
                <h3>$180.00</h3>
                <p>VIP年度会员</p>
                <ul class="list-unstyled">
                  <li>年度5折巨惠</li>
                  <li>极速批量化操作</li>
                  <li>海量数据无限制导入</li>
                  <li>客服7×24小时紧急支持</li>·
                  <li>新功能首发体验资格</li>
                  <li>狂省$180，日均仅需$0.49</li>
                  <li>订阅即赠月度会员</li>
                </ul><!-- /.list-unstyled -->
                <a href="https://t.me/dingdangtw" target="_blank" class="thm-btn pricing-one__btn"><span>前往充值</span></a>
                <span class="tag-line">应用内支持自动充值</span>
              </div><!-- /.pricing-one__single -->
            </div><!-- /.col-lg-4 -->
          </div><!-- /.row -->
        </div><!-- /#month -->
      </div><!-- /.tabed-content -->
    </div><!-- /.container -->
  </section>
</template>

<script>
export default {
  name: "Pricing",
  mounted() {

    function toggleTabWithSwitch() {
      var toggleSwitch = $('#switch-toggle-tab label.switch');
      var monthTabTitle = $('#switch-toggle-tab li.month');
      var yearTabTitle = $('#switch-toggle-tab li.year');
      var monthTabContent = $('#month');
      var yearTabContent = $('#year');
      // hidden show deafult;
      monthTabContent.fadeIn();
      yearTabContent.fadeOut();

      function toggleHandle() {
        if (toggleSwitch.hasClass('on')) {
          yearTabContent.fadeOut();
          monthTabContent.fadeIn();
          monthTabTitle.addClass('active');
          yearTabTitle.removeClass('active');
        } else {
          monthTabContent.fadeOut();
          yearTabContent.fadeIn();
          yearTabTitle.addClass('active');
          monthTabTitle.removeClass('active');
        }
      };
      monthTabTitle.on('click', function () {
        toggleSwitch.addClass('on').removeClass('off');
        toggleHandle();
        return false;
      });
      yearTabTitle.on('click', function () {
        toggleSwitch.addClass('off').removeClass('on');
        toggleHandle();
        return false;
      });
      toggleSwitch.on('click', function () {
        toggleSwitch.toggleClass('on off');
        toggleHandle();
      });

    }

    toggleTabWithSwitch();
  }

}
</script>

<style scoped>

</style>
