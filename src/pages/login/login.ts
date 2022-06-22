import { createApp } from 'vue'
import Login from './App_login.vue'
import 'element-plus/dist/index.css'
import VueCookies from 'vue-cookies';


import { ElButton, ElContainer, ElFooter, ElForm, ElFormItem, ElHeader, ElInput, ElMain, ElPopover, } from "element-plus";

const App_login = createApp(Login)
App_login
    .use(VueCookies)
    .use(ElForm)
    .use(ElInput)
    .use(ElFormItem)
    .use(ElButton)
    .use(ElPopover)
    .use(ElContainer)
    .use(ElMain)
    .use(ElHeader)
    .use(ElFooter)

    .mount('#app')
