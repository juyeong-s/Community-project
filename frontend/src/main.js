// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from "axios";
import Header from "./components/Header.vue";
import Content from "./components/Content.vue";
import Footer from "./components/Footer.vue";

// let url = "http://127.0.0.1:8000/community/getlist/";

// export default {
//   data(){
//     return {
//       userList: [],
//       postList: []
//     }
//   },
//   components: {
//     Header,
//     Content,
//     Footer
//   },
  
// }

// axios.get(url)
//  .then((res)=>{
//   console.log(res)
// })
// .catch((err)=>{
//   console.log(err)
// })

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
