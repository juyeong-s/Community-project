<template>
<div class="main">
  <div class="header">
    <img class="logo" alt="Vue logo" src="./assets/logo.png">
  </div>
  <div class="content">
    <!-- <PostList /> -->
    <router-view></router-view>
    <!-- <router-link to="/list"></router-link> -->
  </div>

  <div class="footer">
    <p>footer에요</p>
  </div>
</div>
</template>

<script>
import PostList from './components/PostList.vue'

export default {
  name: 'App',
  components: {
    PostList

  }
}
</script>

<style>
#app {
  font-family: 'Do Hyeon', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.main{
  text-align: center;
}
.logo{
  width: 80px;
  height: 80px;
}
/* .content{
} */
.footer{
  background-color: rgb(209, 247, 194);
  width: 100%;
  position: absolute;
  bottom: 1%;
}
</style>
