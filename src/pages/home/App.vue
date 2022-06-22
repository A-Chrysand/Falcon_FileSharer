<template>
	<GameNav parm_navTitle=" " :parm_routerLinkList="routerLinkList" />
	<div id="MainContent">
		<router-view />
	</div>
</template>

<script lang="ts">
import GameNav from "@/components/nav/PotatoNav.vue";
import ignister from "@/pages/store";
import { defineComponent } from "vue";
export default defineComponent({
	name: "App_potato",
	data() {
		return {
			routerLinkList: [
				{
					//FullName: "<i class='bi bi-activity'></i>Home",
					FullName: "<i class='el-icon-download'></i> 下载",
					ShortName: "🔥",
					Link: ignister.nginx_baseUrl() + "download",
				},
				{
					FullName: "<i class='el-icon-upload2'></i> 上传",
					ShortName: "⭐",
					Link: ignister.nginx_baseUrl() + "upload",
				},
				{
					FullName: "<i class='el-icon-loading'></i> Home",
					ShortName: "😰",
					Link: ignister.nginx_baseUrl() + "index",
				},
			],
		};
	},
	methods: {},
	components: {
		GameNav,
	},
	mounted() {
		this.$router.push({ name: "Download" });
	},
	unmounted() {
		this.$cookies.set("", "", -1);
	},
});
</script>

<style lang="sass">
@import @/components/viewport
@import @/components/component
#MainContent
	margin-top: $component_navHeight
	@media #{$pc}	  //电脑
		margin-left: 200px
	@media #{$tablet}	  //平板
		margin-left: 50px
	@media #{$mobile}	  //手机
		margin-left: 0px
</style>