import Vue from 'vue'
import App from './App.vue'
import router from '../router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import ElementUI, {Message} from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import *as echarts from 'echarts';
import 'default-passive-events'
Vue.prototype.$echarts = echarts;
Vue.use(ElementUI);
Vue.use(router);
Vue.use(VueAxios, axios)
Vue.use(axios);
// Vue.prototype.axios = axios

Vue.prototype.$message = function (msg){
  return Message({
    message:msg,
    duration:1500
  })
}
Vue.prototype.$message.success = function (msg) {
  return Message.success({
    message: msg,
    duration: 1500
  })
}
Vue.prototype.$message.error = function (msg) {
  return Message.error({
    message: msg,
    duration: 1500
  })
}
Vue.prototype.$message.warning = function (msg) {
  return Message.warning({
    message: msg,
    duration: 1500
  })
}
Vue.prototype.$message.info = function (msg) {
  return Message.info({
    message: msg,
    duration: 1500
  })
}
new Vue({
  el:"#app",
  router,
  render:h=>h(App)
}).$mount('#app')
