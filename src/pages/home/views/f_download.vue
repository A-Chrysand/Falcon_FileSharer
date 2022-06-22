<template>
	<div id="container_fileDownload">
		<table class="table_file_list">
			<tr>
				<th class="list_name">文件名</th>
				<th class="list_size">大小</th>
				<!--th class="list_manage">操作</th-->
			</tr>
			<tr v-for="fileitems in fileList" :key="fileitems">
				<td class="list_name">
					<a :href="fileitems.url" :style="'padding-left:' + fileitems.layer + 'em'"
						:download="fileitems.filename"><span
							v-html="addAIcon(fileitems.type)"></span>{{ fileitems.filename }}</a>
				</td>
				<!--  TODO v-for配合computed 使用 -->
				<td class="list_size">{{ fileitems.size }}</td>
				<!--td class="list_manage">
					<span class="span_manage_rename"
						@click="InitRrenameFile(fileitems.fileURL)">重命名</span>
					<span>&emsp;</span>
					<span class="span_manage_delete"
						@click="DeleteFile(fileitems.fileURL)">删除</span>
				</td-->
			</tr>
		</table>
		<p style="margin: 0">&ensp;{{ msg }}</p>
	</div>
	<div id="div_Rename" v-if="displayRenameAlertWindow">
		您确定要重命名吗？
		<input type="text" name="" id="" v-model="tempNewName" />
		<p>*不支持修改拓展名*</p>
		<button @click="RrenameFile(tempNewName, tempURL)">确定</button>
		&emsp;
		<button @click="displayRenameAlertWindow = false">取消</button>
	</div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import store from "@/pages/store";
import axios from "axios";
export default defineComponent({
	name: "f_Download",
	data(): any {
		return {
			displayRenameAlertWindow: false,
			tempNewName: "none",
			tempURL: "",
			msg: "完毕",
			//fileList: [],
			fileList: this.getFileList(),
		};
	},
	computed: {},
	methods: {
		addAIcon(parm: string): string {
			if (parm == "dir") {
				return '<i class="el-icon-folder-opened"></i>';
			} else {
				return "";
			}
		},
		InitRrenameFile(i_url: string): void {
			this.displayRenameAlertWindow = true;
			this.tempURL = i_url;
		},
		RrenameFile(fileName: string, i_url: string): void {
			axios
				.post(
					"/file_manage/rename?filename=" +
						fileName +
						"&fileTarget=" +
						i_url
				)
				.then((response) => {
					if (response.status == 401) {
						window.location.href =
							store.nginx_baseUrl() + "/login.html";
					}
					alert(response.data);
					this.displayRenameAlertWindow = false;
					this.getFileList();
				});
		},
		DeleteFile(fileUrl: string): void {
			let flag = confirm("您确定要删除" + fileUrl + "吗？");
			if (flag) {
				axios
					.post("/file_manage/delete?targetFile=" + fileUrl)
					.then((response) => {
						alert(response.data);
						this.getFileList();
					});
			}
		},
		getFileList(): unknown {
			axios
				.get(store.nginx_baseUrl() + "jsGet/share/filetree", {
					headers: {
						Gexempt: "vue-request-f_download",
					},
				})
				.then((response) => {
					//console.log("AXIOSING");
					//console.log(response);
					this.fileList = response.data;
					//this.$forceUpdate();
				})
				.catch((error) => {
					console.log(error);
					if (error.toString().indexOf("401") != -1) {
						alert("检测到未登陆，立即跳转到登录页面");
						window.location.href =
							store.nginx_baseUrl() + store.login_url;
					}
				});
			return [
				{
					fileName: "tempFileName",
					fileSize: "0.0KB",
					fileURL: "#13",
				},
			];
		},
	},
	mounted() {
		//this.getFileList();
	},
});
</script>

<style lang="sass">
.div_header
  display: flex
.div_fileForm
  position: absolute
  right: 0
.table_file_list
  margin-bottom: 0
  border-collapse: collapse
  border-right: 1px solid rgba(0,0,0,0.1)
  border-bottom: 1px solid rgba(0,0,0,0.1)
td, th
  padding: 12px
  border-collapse: collapse
  white-space: nowrap
th
  text-align: center
td
  text-align: left
  border-top: 1px solid rgba(0,0,0,0.1)
.list_size
  max-width: 4rem
.list_name
  width: 100%
.list_manage
.span_manage_rename,.span_manage_delete
	cursor: pointer
.span_manage_rename
	color: blue
.span_manage_delete
	color: red

#div_Rename
  padding: 1rem
  width: 200px
  height: 90px
  background: rgba(240, 220, 140,0.97)
  border: 1px solid aqua
  border-radius: 10px
  position: absolute
  text-align: center
  z-index: 990
  transform: translate(-50%,-50%)
  top: 50%
  left: 50%
p
  margin: 0
  font-size: 8px
  color: red
  text-align: left
  text-indent: 1rem
input
  margin-top: 0.5rem
</style>