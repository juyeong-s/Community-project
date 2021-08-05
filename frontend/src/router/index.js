import Vue from 'vue'
import Router from 'vue-router'
import PostList from '../components/PostList.vue'
import PostDetail from '../components/PostDetail.vue'
import PostForm from '../components/PostForm.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/list',
      name: 'PostList',
      component: PostList,
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
    }
  ]
})
