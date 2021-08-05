<template>
  <div>
      <Header class="header"></Header>
      <Content class="content" :postlist="postlist"></Content>
      <Footer class="footer"></Footer>
    </div>
</template>

<script>
import axios from "axios"
// import PostList from './components/PostList.vue'
import Header from "./components/Header.vue"
import Content from "./components/Content.vue"
import Footer from "./components/Footer.vue"
let posturl = "http://127.0.0.1:8000/community/getPostlist/";
let userurl = "http://127.0.0.1:8000/community/getUserlist/";

export default {
  name: 'App',
  data(){
      return{
        postlist : [],
        userlist: []
      }
  },
  components: {
      Header: Header,
      Content: Content,
      Footer: Footer
  },
  mounted() {
    axios({
      method: "GET",
      url: posturl 
    })
    .then(response => {
      this.postlist = response.data;
      console.log(this.postlist)
    })
    .catch(response => {
      console.log("Failed", response);
    });

    axios({
      method: "GET",
      url: userurl 
    })
    .then(response => {
      this.userlist = response.data;
      console.log(this.userlist)
    })
    .catch(response => {
      console.log("Failed", response);
    });
  },
  methods: {  // CRUD 로직 
    getUserList() {

    },
    updateUserList() {

    },
    deleteUserList() {

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
.header{
  /* text-align: center; */
}

.footer{
  background-color: rgb(209, 247, 194);
  width: 100%;
  height: 5%;
  position: absolute;
  bottom: 1%;
  text-align: center;
}
</style>
