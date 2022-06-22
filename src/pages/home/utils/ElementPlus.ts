import { App } from 'vue'
import "element-plus/dist/index.css"
import {
    ElIcon,
    //ElSwitch,
    ElUpload,
    //ElInput,
    //ElButton, ElMessage
} from 'element-plus'

export default function ElComponentImporter(app: App): App {
    [
        ElIcon,
        //ElSwitch,
        ElUpload,
        //ElInput,
        //ElButton, ElMessage

    ].forEach((v) => {
        app.use(v)
    })
    return app
}
