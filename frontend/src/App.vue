<template>
<div class="main">
  <div class="header">
    <img class="logo" alt="Vue logo" src="./assets/logo.png">
  </div>
  <div class="content">
    <button @click="getData">게시물 조회</button>
    {{ data }}
    <!-- <PostList /> -->
    <router-view></router-view>
    <router-link to="/list" @click="getData"></router-link>
  </div>

  <div class="footer">
    <p>footer에요</p>
  </div>
</div>
</template>

<script>
import axios from "axios"
import PostList from './components/PostList.vue'

export default {
  name: 'App',
  data(){
    return {
      userList : []
    }
  },
  components: {
    PostList
  },
  methods: {
    getData(){
      axios.get("http://127.0.0.1:8000/community/post/")
      .then((res)=>{
        for(let i of res.data){
          this.userList.push({
            id: i.pk,
            title: i.fields.title,
            writer_fk_id: i,
            content: i.fields.content,
            created_dt: i.fields.created_dt,
            modified: i.fields.modified
          })
        }
      })
      .catch((err)=>{
        alert(err);
      })
    }
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
