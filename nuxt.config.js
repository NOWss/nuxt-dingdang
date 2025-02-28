require('dotenv').config();
const { from } = require('env-var');
const env = from(process.env);

export default {
  mode: 'universal',
  // ✨ 注入公共环境变量到客户端
  publicRuntimeConfig: {
    API_BASE: env.get('NUXT_PUBLIC_API_BASE').required().asString(),
  },
  /*
  ** Headers of the page
  */
  head: {
    title: process.env.npm_package_name || '',
    meta: [
      {charset: 'utf-8'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1'},
      {hid: 'description', name: 'description', content: process.env.npm_package_description || ''}
    ],
    link: [
      {rel: 'icon', type: 'image/x-icon', href: '/assets/images/favicons/favicon.ico'},
      {rel: 'apple-touch-icon', sizes: '180x180', href: '/assets/images/favicons/apple-touch-icon.png'},
      {rel: 'icon', type: 'image/png', sizes: '32x32', href: '/assets/images/favicons/favicon-32x32.png'},
      {rel: 'icon', type: 'image/png', sizes: '16x16', href: '/assets/images/favicons/favicon-16x16.png'},
      {rel: 'stylesheet', href: '/assets/fonts/iconfont.css'},
      {
        rel: "stylesheet",
        href:
          "https://fonts.googleapis.com/css?family=Rubik:300,400,500,700,900&display=swap"
      },
      {rel: "stylesheet", href: "/assets/css/bootstrap.min.css"},
      {rel: "stylesheet", href: "/assets/css/animate.min.css"},
      {rel: "stylesheet", href: "/assets/css/owl.carousel.min.css"},
      {rel: "stylesheet", href: "/assets/css/owl.theme.default.min.css"},
      {rel: "stylesheet", href: "/assets/css/magnific-popup.css"},
      {rel: "stylesheet", href: "/assets/css/font-awesome.min.css"},
      {rel: "stylesheet", href: "/assets/css/swiper.min.css"},
      {rel: "stylesheet", href: "/assets/plugins/dimon-icons/style.css"},
      {rel: "stylesheet", href: "/assets/css/style.css"},
      {rel: "stylesheet", href: "/assets/css/responsive.css"},
    ],

    script: [
      {src: "/assets/js/jquery.min.js", type: "text/javascript", body: true},
      {src: "/assets/js/bootstrap.bundle.min.js", type: "text/javascript", body: true},
      {src: "/assets/js/owl.carousel.min.js", type: "text/javascript", body: true},
      {src: "/assets/js/waypoints.min.js", type: "text/javascript", body: true},
      {src: "/assets/js/jquery.counterup.min.js", type: "text/javascript", body: true},
      {src: "/assets/js/TweenMax.min.js", type: "text/javascript", body: true},
      {src: "/assets/js/wow.js", type: "text/javascript", body: true},
      {src: "/assets/js/jquery.magnific-popup.min.js", type: "text/javascript", body: true},
      {src: "/assets/js/jquery.ajaxchimp.min.js", type: "text/javascript", body: true},
      {src: "/assets/js/swiper.min.js", type: "text/javascript", body: true},
      {src: "/assets/js/jquery.easing.min.js", type: "text/javascript", body: true},
    ]
  },
  /*
  ** Customize the progress-bar color
  */
  loading: {color: '#fff'},
  /*
  ** Global CSS
  */
  css: [],
  /*
  ** Plugins to load before mounting the App
  */
  plugins: [],
  /*
  ** Nuxt.js dev-modules
  */
  buildModules: [],
  /*
  ** Nuxt.js modules
  */
  modules: [],
  /*
  ** optimizedImages
  */
  optimizedImages: {
    optimizeImages: true
  },

  /*
  ** Build configuration
  */
  build: {
    /*
    ** You can extend webpack config here
    */
    extend(config, ctx) {
    },
    babel: {
      plugins: [
        '@babel/plugin-proposal-optional-chaining'
      ]
    }
  },
  server: {
    host: '0.0.0.0',  // 绑定到所有网络接口，允许局域网内的其他设备访问
    port: 3000,       // 你可以指定端口，默认是 3000
  }
}
