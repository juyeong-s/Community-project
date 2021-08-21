  
// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Vuetify from 'vuetify'
import store  from './store.js'
import VueMoment from 'vue-moment'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
// import CKEditor from 'ckeditor4-vue';
import CKEditor from '@ckeditor/ckeditor5-vue2'

Vue.use( CKEditor );
Vue.use(VueMoment);
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.use(Vuetify);

Vue.config.productionTip = false

export default new Vue({
  el: '#app',
  router,
  components: { App },
  store,
  template: '<App/>',
  vuetify: new Vuetify(),
  CKEditor,
  render: h => h(App)
}).$mount('#app');