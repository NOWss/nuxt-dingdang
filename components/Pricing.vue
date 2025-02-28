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
            <div class="col-lg-4 wow fadeInUp" data-wow-duration="1500ms">
              <div class="pricing-one__single text-center">
                <h3>$30.00</h3>
                <p>VIP月度会员</p>
                <ul class="list-unstyled">
                  <li>解锁全部高级功能，畅享极致效率体验</li>
                  <li>单次最大4G文件导入/导出</li>
                  <li>百万组任务秒级处理完成</li>
                  <li>专属顾问+7×24小时紧急支持</li>
                  <li>新功能首发体验资格</li>
                  <li>订阅即赠10天有效期</li>
                </ul><!-- /.list-unstyled -->
                <a href="https://t.me/dingdangtw" target="_blank" class="thm-btn pricing-one__btn"><span>前往充值</span></a>
                <span class="tag-line">没有额外收费!</span>
              </div><!-- /.pricing-one__single -->
            </div><!-- /.col-lg-4 -->
            <div class="col-lg-4 wow fadeInDown" data-wow-duration="1500ms">
              <div class="pricing-one__single text-center">
                <h3>$72.00</h3>
                <p>VIP季度会员</p>
                <ul class="list-unstyled">
                  <li>尊享8折超值优惠，精准数据一键获取</li>
                  <li>单次最大4G文件导入/导出</li>
                  <li>百万组任务秒级处理完成</li>
                  <li>专属顾问+7×24小时紧急支持</li>
                  <li>新功能首发体验资格</li>
                  <li>超值省$18：轻松提升效率，成本直降</li>
                  <li>订阅即赠20天有效期</li>
                </ul><!-- /.list-unstyled -->
                <a href="https://t.me/dingdangtw" target="_blank" class="thm-btn pricing-one__btn"><span>前往充值</span></a>
                <span class="tag-line">没有额外收费!</span>
              </div><!-- /.pricing-one__single -->
            </div><!-- /.col-lg-4 -->
            <div class="col-lg-4 wow fadeInUp" data-wow-duration="1500ms">
              <div class="pricing-one__single text-center">
                <h3>$180.00</h3>
                <p>VIP年度会员</p>
                <ul class="list-unstyled">
                  <li>年度5折巨惠，打造行业竞争力</li>
                  <li>无限制导入/导出，工作流畅如飞 </li>
                  <li>百万组任务秒级处理完成</li>
                  <li>专属顾问+7×24小时紧急支持</li>
                  <li>新功能首发体验资格</li>
                  <li>狂省$180：日均仅需$0.49</li>
                  <li>订阅即赠月度会员，尊享全年无忧服务</li>
                </ul><!-- /.list-unstyled -->
                <a href="https://t.me/dingdangtw" target="_blank" class="thm-btn pricing-one__btn"><span>前往充值</span></a>
                <span class="tag-line">没有额外收费!</span>
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
          monthTabTitle.on('click', function() {
            toggleSwitch.addClass('on').removeClass('off');
            toggleHandle();
            return false;
          });
          yearTabTitle.on('click', function() {
            toggleSwitch.addClass('off').removeClass('on');
            toggleHandle();
            return false;
          });
          toggleSwitch.on('click', function() {
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
