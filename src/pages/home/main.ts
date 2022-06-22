import { createApp } from 'vue'
import RubbishBin from './App.vue'
import RubbishBinRouter from "./utils/router"
import ElComponentImporter from "@/pages/home/utils/ElementPlus"
import "./style/bs_tweak.sass"
import 'element-ui/lib/theme-chalk/index.css';


const App_home = createApp(RubbishBin)
ElComponentImporter(App_home)
App_home
    .use(RubbishBinRouter)
    .mount('#app')
