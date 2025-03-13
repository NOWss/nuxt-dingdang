<template>
  <div class="post-pagination">
    <nuxt-link
      v-if="currentPage > 1"
      :to="generateLink(currentPage - 1)"
      :class="{ 'active': currentPage === currentPage - 1 }"
      :aria-disabled="currentPage === 1 ? 'true' : 'false'"
    >
      <i class="fa fa-angle-double-left"></i>
    </nuxt-link>

    <!-- Disabled Previous page link -->
    <a
      v-else
      :class="{ 'disabled': true }"
      :aria-disabled="true"
      href="javascript:void(0)"
    >
      <i class="fa fa-angle-double-left"></i>
    </a>

    <!-- Pages list -->
    <nuxt-link
      v-for="page in pagination"
      v-if="page !== '...'"
      :key="page"
      :to="generateLink(page)"
      :class="{ 'active': page === currentPage }"
    >
      {{ page }}
    </nuxt-link>
    <span class="dot" v-else>{{ page }}</span> <!-- 这里显示省略号 -->

    <!-- Next page link -->
    <nuxt-link
      v-if="currentPage < totalPages"
      :to="generateLink(currentPage + 1)"
      :class="{ 'active': currentPage === currentPage + 1 }"
      :aria-disabled="currentPage === totalPages ? 'true' : 'false'"
    >
      <i class="fa fa-angle-double-right"></i>
    </nuxt-link>

    <!-- Disabled Next page link -->
    <a
      v-else
      :class="{ 'disabled': true }"
      :aria-disabled="true"
      href="javascript:void(0)"
    >
      <i class="fa fa-angle-double-right"></i>
    </a>
  </div>
</template>

<script>
export default {
  name: "pagination",
  props: {
    totalItems: {
      type: Number,
      required: true
    },
    itemsPerPage: {
      type: Number,
      required: true
    },
    currentPage: {
      type: Number,
      required: true
    }
  },
  computed: {
    totalPages() {
      return Math.ceil(this.totalItems / this.itemsPerPage);
    },
    pagination() {
      let pages = [];
      const maxVisiblePages = 5; // 可见的最大页数
      const currentPage = this.currentPage;

      // 如果总页数小于最大可显示页数，直接显示所有页码
      if (this.totalPages <= maxVisiblePages) {
        for (let i = 1; i <= this.totalPages; i++) {
          pages.push(i);
        }
        return pages;
      }

      // 前几页和省略号逻辑
      if (currentPage <= 3) {
        for (let i = 1; i <= 4; i++) {
          pages.push(i); // 显示 1, 2, 3, 4
        }
        pages.push('...');
        pages.push(this.totalPages); // 最后一页
      } else if (currentPage >= this.totalPages - 2) {
        pages.push(1); // 显示第一页
        pages.push('...');
        for (let i = this.totalPages - 3; i <= this.totalPages; i++) {
          pages.push(i); // 显示倒数三页
        }
      } else {
        pages.push(1); // 显示第一页
        pages.push('...');
        for (let i = currentPage - 1; i <= currentPage + 1; i++) {
          pages.push(i); // 显示当前页前后各一页
        }
        pages.push('...');
        pages.push(this.totalPages); // 最后一页
      }

      return pages;
    }
  },
  methods: {
    generateLink(page) {
      // 获取当前查询参数，包括可能存在的其他参数
      const queryParams = { ...this.$route.query, page };

      // 如果你不需要 `tag` 参数，可以通过删除它来去除
      if (!queryParams.tag) {
        delete queryParams.tag;
      }

      return {
        path: '/blog',  // 路径可以根据实际情况调整
        query: queryParams  // 动态传递 query 参数
      };
    }
  }
}
</script>

<style scoped>
.dot{
  padding: 5px 10px;
}

a{
  color: #0b0b0b;
}

a.disabled {
  color: #ccc;
  cursor: not-allowed;
}
</style>
