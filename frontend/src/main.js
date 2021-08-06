// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import vuetify from './plugins/vuetify'
import store  from './store.js'
import VueMoment from 'vue-moment'
Vue.use(VueMoment);
// app.use(store).mount('#app')

Vue.config.productionTip = false

/* eslint-disable no-new */
export default new Vue({
  el: '#app',
  router,
  components: { App },
  vuetify,
  store,
  template: '<App/>',
  render: h => h(App)
}).use(store).$mount('#app')
