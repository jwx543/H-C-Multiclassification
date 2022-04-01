import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const constantRoutes = [
    {
        path: '/',
        component: resolve => require(['../pages/Hello'], resolve)
    }
]

export default new Router({
    mode: 'history',
    scrollBehavior: () => ({x: 0, y: 0}),
    routes: constantRoutes
})
