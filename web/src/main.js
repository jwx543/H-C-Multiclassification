import Vue from 'vue'
import App from './App'
import router from './router'
import Vuex from 'vuex'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.use(Vuex)
Vue.use(ElementUI)


new Vue({
  el: '#app',
  router: router,
  render: h => h(App)
})
