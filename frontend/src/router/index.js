import Vue from 'vue'
import Router from 'vue-router'
import PostList from '@/components/PostList'
import PostDetail from '@/components/PostDetail'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/list',
      name: 'PostList',
      component: PostList
    },
    {
      path: '/detail/:id',
      name: 'PostDetail',
      component: PostDetail
    }
  ]
})
