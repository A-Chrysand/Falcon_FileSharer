<template>
	<!-- TODO [4] 导航栏底部在移动端不显示 -->
	<nav id="Container_Navbar">
		<div class="Horzional">
			<div class="nav-item left">
				<!-- empty -->
			</div>
			<div class="middle">
				<span class="middle-title">{{ parm_navTitle }}</span>
			</div>
			<div class="nav-item right">
				<span>欢迎</span>
				<span v-html="client_ip"></span>
			</div>
		</div>
		<aside class="aside" :class="AsideIsOpen ? 'AsideIsOpen' : ''">
			<HambugerButton :parm_bool_AsideIsOpen="AsideIsOpen" parm_string_width="2rem"
				@click="AsideIsOpen = !AsideIsOpen" />
			<div>
				<div class="div_asideRouterLink" v-for="navitems in parm_routerLinkList"
					:key="navitems">
					<router-link class="routerlink wide" :to="navitems.Link"
						v-html="navitems.FullName">
					</router-link>
					<router-link class="routerlink narrow" :to="navitems.Link"
						v-html="navitems.ShortName">
					</router-link>
					<router-link class="routerlink wide subNavItem" :to="subNavItems.Link"
						v-for="subNavItems in navitems.childend" :key="subNavItems"
						v-html="subNavItems.FullName">
					</router-link>
				</div>
			</div>
			<div class="div_asideRouterLink bottom">
				<div>
					<a class="routerlink wide" :href="nginx_baseUrl">返回主页 </a>
					<a class="routerlink narrow" :href="nginx_baseUrl">🚕 </a>
				</div>
				<div>
					<a class="routerlink wide" :href='nginx_baseUrl+"login.html"'>login </a>
					<a class="routerlink narrow" :href='nginx_baseUrl+"login.html"'>L </a>
				</div>

			</div>
		</aside>
		<AsideMask :parm_bool_AsideIsOpen="AsideIsOpen" @click="AsideIsOpen=!AsideIsOpen" />
	</nav>
</template>


<script lang="ts">
import HambugerButton from "@/components/Item/HambugerButton.vue";
import AsideMask from "@/components/nav/Aside-mask.vue";
import { defineComponent } from "vue";
import store from "@/pages/store";
export default defineComponent({
	name: "GameNav",
	data(): any {
		return {
			AsideIsOpen: false,
			client_ip: this.GetIP(),
			nginx_baseUrl: store.nginx_baseUrl(),
		};
	},
	methods: {
		GetIP() {
			let xhr_getClientIp = new XMLHttpRequest();
			xhr_getClientIp.open(
				"GET",
				store.nginx_baseUrl() + "jsGet/potato/clientip"
			);
			xhr_getClientIp.responseType = "text";
			xhr_getClientIp.send();
			// eslint-disable-next-line @typescript-eslint/no-this-alias
			const that = this;
			xhr_getClientIp.onreadystatechange = function () {
				if (xhr_getClientIp.status === 200) {
					that.client_ip = xhr_getClientIp.response;
				}
			};
		},
	},
	components: {
		HambugerButton,
		AsideMask,
	},
	props: {
		parm_navTitle: {
			type: String,
			default: "title",
		},
		parm_routerLinkList: {
			type: Array,
			default: () => [
				{
					FullName: "nav1",
					ShortName: "N",
					Link: "/",
					childend: [
						{
							FullName: "sn1",
							Link: "/",
						},
					],
				},
			],
		},
	},
});
</script>
<style scoped lang='sass'>
@import @/components/component
@import @/components/viewport
$Nav_backgroundColor: #519AF3
$Aside_backgroundColor: #A6D8FF
$border_color_hor: #0a68ff
$border_color_ver: rgba(122, 198, 255,0.75)
$AsideAnimateTime: 0.2s
#Container_Navbar
	position: fixed
	box-sizing: border-box
	top: 0
	z-index: $layer_navbar
	font-weight: bold
	.Horzional
		position: inherit
		width: 100%
		box-sizing: border-box
		z-index: $layer_navbar
		height: $component_navHeight

		padding-left: 0.5rem
		padding-right: 0.5rem

		display: flex
		justify-content: center
		align-items: center
		background: $Nav_backgroundColor
		box-sizing: border-box
		border-bottom: 1px solid $border_color_hor
		.nav-item
			position: absolute
			margin: auto 0.5rem
			&.right
				right: 0

	.aside
		z-index: inherit
		position: absolute
		top: $component_navHeight
		height: calc(100vh - #{$component_navHeight})
		overflow-x: hidden
		background: $Aside_backgroundColor
		border-right: 1px solid $border_color_ver
		transition: width 0.2s ease-in-out
		@media #{$pc}						//电脑
			text-indent: 1rem
			width: 200px !important
			.routerlink.narrow
				display: none
		@media #{$tablet}	//平板
			width: 50px
			.routerlink.wide
				display: none

		@media #{$mobile}					//手机
			width: 0px
			border-right: none
			a, router-link
				display: none

		&.AsideIsOpen
			text-indent: 1rem
			width: 200px
			.routerlink.wide
				display: block
			.routerlink.narrow
				display: none
			.bottom
				left: 0
				line-height: 3rem
		.hamburger
			position: fixed
			z-index: $layer_hambuger
			top: 9px
			left: 0.5rem
			@media #{$pc}
				display: none

		.bottom
			position: absolute
			width: inherit

			bottom: 0

	.left
		#AsideButton
			display: none
			cursor: pointer
			@media (max-width:$lg_mi)
				display: block

	.middle
		.middle-title
			font-size: 2rem
			font-weight: bolder
			line-height: inherit
			letter-spacing: 0.125rem

	a,.routerlink
		text-align: left
		text-decoration: none
		font-size: 1.25rem
		padding: 0.25em
		display: block
		word-wrap: normal
		word-break: keep-all
		white-space: nowrap
		&, &:visited
			color: rgb(80, 100, 220)
		&:hover
			background-color: #ffdc93
			color: #ff9900
		&.subNavItem.a-exact-active
			background-color: rgb(250,250 ,200)
			color: orange
			// What's the true class name???
		&.subNavItem
			font-size: 1rem
			text-indent: 2rem
		&.narrow
			text-align: center

	.router-link-active, .router-link-exact-active
		background-color: rgba(250,160 ,190,1)
		color: red
</style>
