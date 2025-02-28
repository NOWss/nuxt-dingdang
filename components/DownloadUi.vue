<template>
  <section class="banner-two" id="download">
    <span class="banner-two__shape-1"></span>
    <span class="banner-two__shape-2"></span>
    <span class="banner-two__shape-3"></span>
    <span class="banner-two__shape-4"></span>
    <div class="banner-two__moc">
      <img src="/assets/images/mocs/banner-moc-2-1.png" alt="全球手机号码智能处理软件"/>
    </div><!-- /.banner-two__moc -->
    <div class="container">
      <div class="row">
        <div class="col-xl-12 col-lg-12">
          <div class="banner-two__content" style="text-align:center;">
            <h1 class="banner-two__title banner_title">全球通讯数据管理专家</h1><!-- /.banner-two__title -->
            <h2 class="banner-two__subtitle">为用户提供批量精选号码和个性化定制工具使用</h2>
            <!-- /.banner-two__text -->
            <a href="#" class="banner-two__btn thm-btn ">
              <span>
                <i class="iconfont icon-windows-fill"></i>
                &nbsp;下载应用
              </span>
            </a><!-- /.thm-btn -->
          </div><!-- /.banner-two__content -->
        </div><!-- /.col-lg-6 -->
      </div><!-- /.row -->
    </div><!-- /.container -->
  </section>
</template>
<script>
export default {
  name: 'DownloadUi',
  head(){
    return {
      title: "叮当助手(全球号）App下载 - 专业的多功能号码处理软件-dingdang",
      meta: [
        {
          hid: 'keywords',
          name: 'keywords',
          content: "叮当助手（全球号)下载，号码处理软件，多功能号码处理工具，号码清洗工具，号码筛选工具，全球号码生成器。"
        },
        {
          hid: 'description',
          name: 'description',
          content: "叮当助手(全球号）App官方下载页面，为您提供多个高效便捷的全球号码处理工具。您可以使用叮当助手(全球号）App对号码数据进行大批量导入、排序乱序、清除非手机号码、号码对比去重、vcf格式导出、按需求筛选、批量添加区号、区分不同国家、智能识别提取等操作处理，并可在线批量生成全球号码、采集最新的公开号码数据，为您的业务发展降本提效。"
        }
      ]
    }
  }
}
</script>
<style scoped>
.banner-two {
  margin-bottom: 0;
  height: 100vh;

  .container {
    padding-top: 180px;
  }

  .banner-two__moc {
    bottom: -170px;
    left: 50%;
    transform: translateX(-50%);
    width: 800px;

    img {
      width: 100%;
    }
  }

  .banner_title {
    margin-bottom: 20px;
    font-size: 54px;
  }


  .banner-two__subtitle {
    font-size: 20px;
    margin-bottom: 50px;
  }

  .banner-two__btn {
    border: 2px solid transparent;
    border-radius: 40px;
    background-clip: padding-box, border-box;
    background-origin: padding-box, border-box;
    background-image: linear-gradient(to right, #343746, #343746), linear-gradient(90deg, #ff4eb5 0%, #ffa065 100%);

    span {
      font-size: 24px;
      display: flex;
      align-items: center;


      i{
        font-size: 30px;
        margin-right: 10px;
      }

      &:hover {
        color: #fff;
      }
    }

    &::before {
      display: none;
    }

    &::after {
    }
  }
}
</style>
