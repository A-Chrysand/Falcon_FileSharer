import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import ignister from "@/pages/store"

const routes: Array<RouteRecordRaw> = [
	{
		path: ignister.nginx_baseUrl() + 'index',
		name: 'Home',
		component: () => import('../views/home.vue')
	},
	{
		path: ignister.nginx_baseUrl() + 'upload',
		name: 'Upload',
		component: () => import('../views/f_upload.vue')
	},
	{
		path: ignister.nginx_baseUrl() + 'download',
		name: 'Download',
		component: () => import('../views/f_download.vue')
	}
]

const router = createRouter({
	history: createWebHistory(process.env.BASE_URL),
	routes
})

export default router
