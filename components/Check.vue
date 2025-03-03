<template>
  <section class="banner-one" id="banner">
    <span class="banner-one__shape-1"></span>
    <span class="banner-one__shape-2"></span>
    <span class="banner-one__shape-3"></span>
    <span class="banner-one__shape-4"></span>
    <div class="container">
      <div class="banner-one__moc">
        <img src="/assets/images/mocs/banner-moc-1-1.png" alt="Awesome Image"/>
      </div><!-- /.banner-one__moc -->
      <div class="row">
        <div class="col-xl-6 col-lg-8">
          <div class="banner-one__content">
            <h1 class="banner-one__title">官方防伪查询</h1><!-- /.banner-one__title -->
            <p class="banner-one__text">Anti-counterfeiting query</p>
            <!-- /.banner-one__text -->
            <form lay-filter="myform" id="myform">
              <div class="top_input1">
                <div class="iput2_wrap">
                  <div class="iput2">
                    <div class="iput_divx">
                      <div class="custom-select2" data-select-name="typeName">
                        <div class="custom-select-trigger">
                          <i class="fa fa-chevron-down"></i>
                          <span class="text">Telegram</span>
                          <span></span>
                        </div>
                        <div class="custom-options">
                          <div class="custom-option" data-value="Telegram">Telegram</div>
                        </div>
                      </div>
                    </div>
                    <div class="iput_div3x"><input name="code" type="text" class="input_textx" value=""
                                                   lay-verify="required" placeholder="请输入账号ID,账号ID前请加@"/>
                    </div>
                  </div>
                  <div>
                    <a class="btn" href="javascript:;" lay-filter="kefuQuery">
                      <span>查询&nbsp;&nbsp;<i class="fa fa-search"></i></span>
                    </a>
                  </div>
                </div>

                <div class="iput2_wrap">
                  <div class="iput2">
                    <div class="iput_divx">
                      <div class="custom-select2" data-select-name="addrType">
                        <div class="custom-select-trigger">
                          <i class="fa fa-chevron-down"></i>
                          <span class="text">TRC20_USDT</span>
                          <span></span>
                        </div>
                        <div class="custom-options">
                          <div class="custom-option" data-value="TRC20_USDT">TRC20_USDT</div>
                          <div class="custom-option" data-value="ERC20_USDT">ERC20_USDT</div>
                        </div>
                      </div>
                    </div>
                    <div class="iput_div3x"><input name="addrCode" type="text" class="input_textx" value=""
                                                   lay-verify="required" placeholder="请输入钱包地址"/></div>
                  </div>
                  <div>
                    <a class="btn" href="javascript:;" lay-filter="addrQuery">
                      <span>查询&nbsp;&nbsp;<i class="fa fa-search"></i></span>
                    </a>
                  </div>
                </div>
              </div>
            </form>
          </div><!-- /.banner-one__content -->
        </div><!-- /.col-lg-6 -->
      </div><!-- /.row -->
    </div><!-- /.container -->
  </section>
</template>

<script>
export default {
  name: "Check",
  mounted() {
    const that = this
    function initCustomSelect(customSelect) {
      const trigger = customSelect.querySelector('.custom-select-trigger');
      const options = customSelect.querySelectorAll('.custom-option');
      const triggerText = trigger.querySelector('.text');
      const selectName = customSelect.dataset.selectName;

      // 创建并隐藏一个原生 select（用于表单提交）
      const hiddenSelect = document.createElement('select');
      hiddenSelect.name = selectName;
      hiddenSelect.style.display = 'none'; // 隐藏原生 select
      options.forEach(option => {
        const nativeOption = document.createElement('option');
        nativeOption.value = option.dataset.value;
        nativeOption.textContent = option.textContent;
        hiddenSelect.appendChild(nativeOption);
      });
      customSelect.appendChild(hiddenSelect);

      // 设置默认值
      const initialOption = customSelect.querySelector('.custom-option.selected') || options[0];
      if (initialOption) {
        initialOption.classList.add('selected');
        triggerText.textContent = initialOption.textContent;
        if (that.$route.query.trc20_usdt){
          triggerText.textContent = 'TRC20_USDT';
        }
        hiddenSelect.value = initialOption.dataset.value;
      }

      // 事件绑定
      trigger.addEventListener('click', () => {
        customSelect.classList.toggle('open');
      });

      options.forEach(option => {
        option.addEventListener('click', () => {
          // 移除之前的选中状态
          options.forEach(opt => opt.classList.remove('selected'));
          // 设置当前选中项
          option.classList.add('selected');
          triggerText.textContent = option.textContent;
          hiddenSelect.value = option.dataset.value; // 同步到原生 select
          customSelect.classList.remove('open');
        });
      });

      // 点击页面其他地方时关闭下拉菜单
      document.addEventListener('click', event => {
        if (!customSelect.contains(event.target)) {
          customSelect.classList.remove('open');
        }
      });
    }

    // 初始化所有自定义 Select 实例
    document.querySelectorAll('.custom-select2').forEach(initCustomSelect);
  }
}
</script>

<style scoped>
.iput2_wrap {
  display: flex;
  justify-content: space-around;
  align-items: center;
  margin-top: 30px;
  border-radius: 50px;
}

.iput2_wrap .btn {
  padding: 0 30px;
  height: 48px;
  background: #2273ED;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-radius: 0 50px 50px 0;
  font-size: 18px;
  font-weight: normal;
}

.iput2_wrap .btn i {
  font-size: 18px;
}

.iput2_wrap a {
  background: #196BEC;
  color: #fff;
}

.iput2_wrap .iput2 {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 48px;
}

.iput2_wrap .iput2 .iput_divx {
  background: #fff;
  height: 48px;
  display: flex;
  width: 156px;
  justify-content: center;
  align-items: center;
  position: relative;
  border-radius: 50px 0 0 50px;
}

.iput2_wrap .iput2 .iput_divx select {
  font-size: 16px;
  border: 0;
  margin: 0 15px;
  text-align: center;
  background: #fff;
  color: #2273ED;
  display: none;
}

.iput2_wrap .iput2 .iput_divx .custom-select2 {
  position: absolute;
  display: inline-block;
  width: 100%;
  font-family: Arial, sans-serif;
}

.iput2_wrap .iput2 .iput_divx .custom-select2 .custom-select-trigger {
  background-color: #fff;
  color: #2273ED;
  padding: 10px 15px;
  border-radius: 4px;
  cursor: pointer;
  display: flex;
  align-items: center;
  border-radius: 50px 0 0 50px;
  justify-content: space-between;
  font-size: 14px;
  user-select: none;
}

.iput2_wrap .iput2 .iput_divx .custom-select2 .custom-select-trigger .text {
  color: #2273ED;
  font-size: 16px;
}

.iput2_wrap .iput2 .iput_divx .custom-select2 .custom-options {
  position: absolute;
  top: 100%;
  left: 0;
  width: 100%;
  background-color: #fff;
  border: 1px solid #2273ED;
  border-radius: 4px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  max-height: 200px;
  overflow-y: auto;
  z-index: 10;
  display: none;
}

.iput2_wrap .iput2 .iput_divx .custom-select2 .custom-options .custom-option {
  padding: 2px 15px;
  cursor: pointer;
  transition: background-color 0.3s;
  font-size: 14px;
}

.iput2_wrap .iput2 .iput_divx .custom-select2 .custom-options .custom-option:hover {
  background-color: #f0f0f0;
}

.iput2_wrap .iput2 .iput_divx .custom-select2 .custom-options .custom-option.selected {
  background-color: #2273ED;
  color: #fff;
  font-weight: bold;
}

.iput2_wrap .iput2 .iput_divx .custom-select2.open .custom-options {
  display: block;
}

.iput2_wrap .iput2 .iput_div3x {
  width: 280px;
  height: 48px;
}

.iput2_wrap .iput2 .iput_div3x input::placeholder {
  color: #196BEC;
  opacity: 0.8;
}

.iput2_wrap .iput2 .iput_div3x input::-webkit-input-placeholder {
  color: #196BEC;
  opacity: 0.8;
}

.iput2_wrap .iput2 .iput_div3x input::-moz-placeholder {
  color: #196BEC;
  opacity: 0.8;
}

.iput2_wrap .iput2 .iput_div3x input:-ms-input-placeholder {
  color: #196BEC;
  opacity: 0.8;
}

.iput2_wrap .iput2 .iput_div3x input::-ms-input-placeholder {
  color: #196BEC;
  opacity: 0.8;
}

.iput2_wrap .iput2 .input_textx {
  width: 100%;
  height: 100%;
  margin-top: 0px;
  font-size: 16px;
  color: #696969;
  border: 0px;
  border-bottom: 1px solid #ddd;
}

.iput2_wrap .iput2 .input_textx:focus {
  border-bottom: 1px solid #2273ED;
}

input:focus-visible {
  outline: none;
}

.iput2_wrap:last-child .iput2 .iput_divx .custom-select2 .custom-select-trigger {
  color: #FF5DA8;
}

.iput2_wrap:last-child .iput2 .iput_divx .custom-select2 .custom-select-trigger .text {
  color: #FF5DA8;
}

.iput2_wrap:last-child .iput2 .iput_divx .custom-select2 .custom-options {
  border: 1px solid #FF5DA8;
}

.iput2_wrap:last-child .iput2 .iput_divx .custom-select2 .custom-options .custom-option:hover {
  background-color: #f0f0f0;
}

.iput2_wrap:last-child .iput2 .iput_divx .custom-select2 .custom-options .custom-option.selected {
  background-color: #FF5DA8;
  color: #fff;
  font-weight: bold;
}

.iput2_wrap:last-child .iput2 .iput_div3x input::placeholder {
  color: #FF5DA8;
  opacity: 0.8;
}

.iput2_wrap:last-child .iput2 .iput_div3x input::-webkit-input-placeholder {
  color: #FF5DA8;
  opacity: 0.8;
}

.iput2_wrap:last-child .iput2 .iput_div3x input::-moz-placeholder {
  color: #FF5DA8;
  opacity: 0.8;
}

.iput2_wrap:last-child .iput2 .iput_div3x input:-ms-input-placeholder {
  color: #FF5DA8;
  opacity: 0.8;
}

.iput2_wrap:last-child .iput2 .iput_div3x input::-ms-input-placeholder {
  color: #FF5DA8;
  opacity: 0.8;
}

.iput2_wrap:last-child .iput2 .iput_div3x .input_textx:focus {
  border-bottom: 1px solid #FF5DA8;
}

.iput2_wrap:last-child .btn {
  background: #FF5DA8;
  border-color: #FF5DA8;
}

.iput2_wrap:last-child .btn::before {
  background: #a884ce;
}

.iput2_wrap:last-child .btn:hover {
  border-color: #FF5DA8;
  background: #FF5DA8 !important;
}

.iput2_wrap option {
  font-size: 15px;
  line-height: 15px;
}
</style>
