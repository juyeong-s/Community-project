import Vue from 'vue'
import Router from 'vue-router'
import PostList from '@/components/PostList'
import PostDetail from '@/components/PostDetail'
import PostForm from '@/components/PostForm'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/list',
      name: 'PostList',
      component: PostList,
      props: true
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
