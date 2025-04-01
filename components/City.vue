<template>
  <section class="banner-one" id="banner">
    <span class="banner-one__shape-1"></span>
    <span class="banner-one__shape-2"></span>
    <span class="banner-one__shape-3"></span>
    <span class="banner-one__shape-4"></span>
    <div class="container" style="padding-top: 200px;">
      <div class="banner-one__moc">
        <img src="/assets/images/mocs/banner-moc-1-2.png" alt="城市区号大全"/>
      </div><!-- /.banner-one__moc -->
      <div class="row">
        <div class="col-xl-12 col-lg-12">
          <div class="banner-one__content">
            <v-card>
              <v-card-title>
                {{ $route.query.country || $route.params.city }}城市区号&nbsp;&nbsp;
                <v-spacer>
                  <nuxt-link to="/area-code">
                    返回
                  </nuxt-link>
                </v-spacer>
                <v-text-field
                  v-model="search"
                  append-icon="mdi-magnify"
                  label="输入城市进行查询"
                  single-line
                  hide-details
                ></v-text-field>
              </v-card-title>
              <v-data-table
                :headers="headers"
                :items="desserts"
                :search="search"
                :items-per-page="itemsPerPage"
                @page-count="pageCount = $event"
                :page.sync="page"
                hide-default-footer
                style="min-height: 538px;"
              >
                <!--                <template v-slot:item.name="{ item }">-->
                <!--                  <div>-->
                <!--                    <span>{{ item.name }}</span>-->
                <!--                  </div>-->
                <!--                </template>-->
                <template v-slot:item.zh_name="{ item }">
                  <span v-if="item.city == item.zh_name">{{ item.zh_name }}</span>
                  <span v-else>{{ item.zh_name }}<span
                    style="color: #999;font-size: 12px;">（{{ item.city }}）</span></span>
                </template>
              </v-data-table>
              <v-pagination
                v-model="page"
                :length="pageCount"
                :total-visible="7"
                circle
              >
              </v-pagination>
            </v-card>
          </div><!-- /.banner-one__content -->
        </div><!-- /.col-lg-6 -->
      </div><!-- /.row -->
    </div><!-- /.container -->
  </section>
</template>
<script>
export default {
  name: 'City',
  props: {
    areas: {  // 定义接收 blogs 的 props
      type: Array | null,
      required: true
    }
  },
  data() {
    return {
      search: '',
      headers: [
        {
          text: '城市名称',
          align: 'start',
          sortable: false,
          value: 'zh_name',
        },
        {text: '城市邮编', value: "postcode", sortable: false},
        {text: '城市区号', value: 'area_code', sortable: false, width: 100},
      ],
      desserts: [],
      page: 1,
      pageCount: 0,
      itemsPerPage: 10,
    }
  },
  mounted() {
    if (this.areas) {
      this.desserts = this.areas
    } else {
      this.desserts = []
    }
    this.pageCount = Math.floor(this.desserts.length / this.itemsPerPage)
  }
}
</script>

<style scoped>
.banner-one__moc {
  bottom: 29%;
}

.banner-one__content {

  :deep(.v-pagination) {
    padding: 10px 20px;
    justify-content: flex-end;
  }

  :deep(.theme--light.v-pagination .v-pagination__item--active) {
    background: #000 !important;
  }

  :deep(.theme--light.v-btn.v-btn--has-bg) {
    background: #F96445 !important;
    color: #fff;
  }
}
</style>
