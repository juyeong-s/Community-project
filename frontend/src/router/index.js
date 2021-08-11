import Vue from 'vue'
import Router from 'vue-router'
import Vuex from 'vuex';
import PostList from '../components/PostList.vue'
import Pagination from '../components/Pagination.vue'
import PostDetail from '../components/PostDetail.vue'
import PostForm from '../components/PostForm.vue'

Vue.use(Router)
Vue.use(Vuex)

export default new Router({
  routes: [
    {
      path: '/list',
      name: 'Pagination',
      component: Pagination,
      props: true,
    },
    {
      path: '/detail/:id',
      name: 'PostDetail',
      component: PostDetail,
      props: true
    },
    {
      path: '/form',
      name: 'PostForm',
      component: PostForm,
      props: true
    },
  ]
})
