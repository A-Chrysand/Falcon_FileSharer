<template>
	<el-container>
		<el-header id="Header">
			<!--a href="/ignister/dist/home">/ignister/dist/home</!--a>
			<a-- href="/ignister/dist/index.html">/ignister/dist/index.html</a-->
			Header
		</el-header>
		<el-main style="display: flex;justify-content: center">
			<div id="container_form">
				<el-form :model="form" status-icon label-width="120px">
					<el-form-item label="Activity name" prop="iusername">
						<el-input id="iusername" v-model="iform.username" />
					</el-form-item>
					<el-form-item label="Password" prop="ipassword">
						<el-input id="ipassword" v-model="iform.password" type="password" />
					</el-form-item>
					<el-form-item label="token">
						<el-popover placement="bottom" title="Title" :width="200" trigger="click">
							<div id="container_nibiru">
								<div class="ig" v-for="(item,i) in imgs" :key="item"
									:style="'background-color:'+item.bgcolor"
									@click="iform.nibiru=i">
								</div>
							</div>
							<span>&ensp;{{iform.nibiru}}</span>
							<template #reference>
								<el-button>Click to activate</el-button>
							</template>
						</el-popover>
					</el-form-item>
					<el-form-item>
						<el-button type="primary" @click="sm">Create</el-button>
						<el-button @click="clearAll">clear</el-button>
					</el-form-item>
				</el-form>
			</div>
		</el-main>

	</el-container>

</template>

<script lang="ts">
import { defineComponent } from "vue";
import axios from "axios";

import store from "@/pages/store";

export default defineComponent({
	name: "Login",
	data(): any {
		return {
			iform: {
				username: "",
				password: "",
				nibiru: "",
			},
			imgs: [
				{ urls: "", bgcolor: "red" },
				{ urls: "", bgcolor: "green" },
				{ urls: "", bgcolor: "blue" },
			],
		};
	},
	methods: {
		clearAll() {
			this.iform.username = "";
			this.iform.password = "";
			this.iform.nibiru = "";
		},

		sm() {
			axios
				.post(store.nginx_baseUrl() + "jsPost/auth/login", {
					headers: {
						Gexempt: "vue-request-f_download",
					},
					union_carrier: this.iform,
				})
				.then((response) => {
					alert(response.data.info);
					this.$cookies.set(
						"nibiru_token",
						response.headers["nibiru_token"],
						{
							expires: "6000",
						}
					);
					window.location.href = response.data.location;
				})
				.catch((error) => {
					alert(error);
				});
		},
	},
});
</script>

<style lang="sass">
#Header
	text-align: center
	margin-bottom: 100px
#container_form
	max-width: 500px
	width: 100%
#container_nibiru
	display: flex
	.ig
		margin: 5px
		width: 60px
		height: 60px
		border: 1px solid black
</style>