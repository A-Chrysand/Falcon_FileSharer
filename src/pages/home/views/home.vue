<template>
  <Title msg="Home" />
  <hr />
  <div id="Container_Home">
    这是一个适用于园区局域网文件分享的软件
    <br />
    前端Vue后端Django
    <br />
    查看源码
    <br />
    前端:
    <a
      target="_blank"
      href="https://github.com/A-Chrysand/localFileSharer/tree/Vue-frontend"
      >https://github.com/A-Chrysand/localFileSharer/tree/Vue-frontend
    </a>
    <br />
    后端:
    <a
      target="_blank"
      href="https://github.com/A-Chrysand/localFileSharer/tree/Django-backend"
      >https://github.com/A-Chrysand/localFileSharer/tree/Django-backend
    </a>
  </div>
  <div>#TODO 文件列表分页</div>
</template>

<script lang="ts">
import Title from "@/components/Item/Title.vue";
import { defineComponent } from "vue";
export default defineComponent({
  components: {
    Title,
  },
});
</script>

<style lang="sass">
#Container_Home
	padding: 0.5rem 2rem
</style>