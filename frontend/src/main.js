// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from "axios";

let url = "http://127.0.0.1:8000/community/post/";

axios.get(url)
.then((res)=>{
  console.log(res)
})
.catch((err)=>{
  console.log(err)
})

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
