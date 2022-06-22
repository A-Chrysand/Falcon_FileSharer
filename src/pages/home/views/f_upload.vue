<template>
	<div class="container_fileUpload">
		<div>
			<ElSwitch v-model="switchStatus" class="mb-2" active-color="rgb(245 196 29)"
				inactive-color="rgb(65 171 252)" active-text="上传到[下载]页面" inactive-text="上传到默认位置" />
		</div>
		<br />
		<el-upload class="upload-demo" drag :action="uploadUrl" multiple :on-success="uploadSuccess"
			:on-error="uploadError" :headers="uploadHeader" method="post" draggable="true">
			<i class="el-icon-light-rain"
				style="font-size: 6rem; margin-top: 1.5rem; margin-bottom: 1rem"></i>
			<!--el-iconclass="el-icon--upload"><upload-filled /></el-iconclass-->
			<div class="el-upload__text">
				Drop file here or <em>click to upload</em>
			</div>
			<template #tip>
				<div class="el-upload__tip">
					请勿上传文件夹，如需上传请先打包<br />
					<strong style="color: red">最大单个文件限制5GB</strong>
				</div>
			</template>
		</el-upload>
	</div>
</template>

<script lang="ts">
import { ElMessage, ElSwitch } from "element-plus";
import store from "@/pages/store";
import { defineComponent } from "vue";
export default defineComponent({
	name: "f_Upload",
	data() {
		return {
			switchStatus: false,
			uploadUrl: store.nginx_baseUrl() + "jsStream/upload/n/",
			uploadHeader: {
				Pexempt: "vue-f_upload", //useless example header
			},
		};
	},
	watch: {
		switchStatus: function () {
			console.log(this.switchStatus);
			if (this.switchStatus) {
				this.uploadUrl = store.nginx_baseUrl() + "jsStream/upload/s/"; //s=share
			} else {
				this.uploadUrl = store.nginx_baseUrl() + "jsStream/upload/n/"; //n=not share
			}
		},
	},
	components: {
		ElSwitch,
	},
	methods: {
		uploadSuccess(response: any, file: typeof Proxy) {
			ElMessage({
				type: "success",
				dangerouslyUseHTMLString: true,
				message: "[" + file.name + "]上传成功",
			});
		},
		uploadError(response: any, file: any) {
			alert(response);
		},
	},
});
</script>

<style lang="sass">
.container_fileUpload
  margin-top: calc(3rem + 5rem)
  justify-content: center
  display: flex
  text-align: center
  flex-direction: column
</style>