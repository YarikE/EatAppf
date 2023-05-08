import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import Main from "@/pages/Main.vue";
import Order from "@/pages/Order.vue";
import History from "@/pages/History.vue";
import Menu from "@/pages/Menu.vue";
import Report from "@/pages/Report.vue";
import Lucky from "@/pages/Lucky.vue";

const router = createRouter({
    routes : [
        { path: '/',
            component: Main,
            name: 'Home'
        },

        { path: '/order',
            component: Order,
            name: 'Order'
        },

        { path: '/history',
            component: History,
            name: "History"
        },

        {
          path: '/menu',
            component: Menu,
            name: 'Menu'
        },
        {
            path: '/lucky',
            component: Lucky,
            name: 'Lucky'
        },
        {
            path: '/report',
            component: Report,
            name: 'Report'
        }
    ],
    history: createWebHistory()
})

const app = createApp(App)
app.use(router)
app.mount('#app')

