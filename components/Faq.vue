<template>
  <section class="faq-one" id="manual">
    <img src="/assets/images/background/faq-one-bg.png" alt="Awesome Image" class="faq-one__bg" />
    <div class="container">
      <div class="block-title text-center">
        <h2 class="block-title__title">叮当助手<span>号码处理</span> <br>操作手册</h2><!-- /.block-title__title -->
      </div><!-- /.block-title -->
      <div class="accrodion-grp" data-grp-name="faq-accrodion">
        <div class="accrodion active wow fadeInUp" data-wow-duration="1500ms" data-wow-delay="0ms">
          <div class="accrodion-inner">
            <div class="accrodion-title">
              <h4>步骤一：</h4>
            </div>
            <div class="accrodion-content">
              <div class="inner">
                <p>下载客户端，点击【号码处理】使用</p>
                <img src="/assets/images/hmcl/1.png" alt="下载客户端，点击【号码处理】使用">
              </div><!-- /.inner -->
            </div>
          </div><!-- /.accrodion-inner -->
        </div>
        <div class="accrodion  wow fadeInUp" data-wow-duration="1500ms" data-wow-delay="100ms">
          <div class="accrodion-inner">
            <div class="accrodion-title">
              <h4>步骤二：</h4>
            </div>
            <div class="accrodion-content">
              <div class="inner">
                <p>支持多次导入本地TXT格式数据，数据可 进行号码排序乱序、去重、清除非手机号 、清除空号、导出等功能</p>
                <img src="/assets/images/hmcl/2.png" alt="支持多次导入本地TXT格式数据，数据可 进行号码排序乱序、去重、清除非手机号 、清除空号、导出等功能">
              </div><!-- /.inner -->
            </div>
          </div><!-- /.accrodion-inner -->
        </div>
        <div class="accrodion wow fadeInUp" data-wow-duration="1500ms" data-wow-delay="200ms">
          <div class="accrodion-inner">
            <div class="accrodion-title">
              <h4>步骤三：</h4>
            </div>
            <div class="accrodion-content">
              <div class="inner">
                <p>筛选功能：可按号码值跟按组合特征对号按组合特征对号码进行精确筛选</p>
                <img src="/assets/images/hmcl/3.png" alt="筛选功能：可按号码值跟按组合特征对号按组合特征对号码进行精确筛选">
              </div><!-- /.inner -->
            </div>
          </div><!-- /.accrodion-inner -->
        </div>
        <div class="accrodion wow fadeInUp" data-wow-duration="1500ms" data-wow-delay="300ms">
          <div class="accrodion-inner">
            <div class="accrodion-title">
              <h4>步骤四：</h4>
            </div>
            <div class="accrodion-content">
              <div class="inner">
                <p>可分批下载数据，导出格式支持TXT/VCF格式</p>
                <img src="/assets/images/hmcl/4.png" alt="可分批下载数据，导出格式支持TXT/VCF格式">
              </div><!-- /.inner -->
            </div>
          </div><!-- /.accrodion-inner -->
        </div>
      </div>
    </div><!-- /.container -->
  </section>
</template>

<script>
    export default {
      name: "Faq",
      mounted() {
        if ($('.accrodion-grp').length) {
          var accrodionGrp = $('.accrodion-grp');
          accrodionGrp.each(function() {
            var accrodionName = $(this).data('grp-name');
            var Self = $(this);
            var accordion = Self.find('.accrodion');
            Self.addClass(accrodionName);
            Self.find('.accrodion .accrodion-content').hide();
            Self.find('.accrodion.active').find('.accrodion-content').show();
            accordion.each(function() {
              $(this).find('.accrodion-title').on('click', function() {
                if ($(this).parent().parent().hasClass('active') === false) {
                  $('.accrodion-grp.' + accrodionName).find('.accrodion').removeClass('active');
                  $('.accrodion-grp.' + accrodionName).find('.accrodion').find('.accrodion-content').slideUp();
                  $(this).parent().parent().addClass('active');
                  $(this).parent().parent().find('.accrodion-content').slideDown();
                };


              });
            });
          });

        }
      }
    }
</script>

<style scoped>

</style>
