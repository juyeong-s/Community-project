<template>
  <div id="app">
    <Header class="header"></Header>
    <Content
      class="content"
      :postlist="postlist"
      :userlist="userlist"
    ></Content>
    <Footer class="footer"></Footer>
  </div>
</template>

<script>
import axios from "axios";
// import PostList from './components/PostList.vue'
import Header from "./components/Header.vue";
import Content from "./components/Content.vue";
import Footer from "./components/Footer.vue";
let posturl = "http://127.0.0.1:8000/community/getPostlist/";
let userurl = "http://127.0.0.1:8000/community/getUserlist/";
// let pagedposturl = "http://127.0.0.1:8000/community/pagedpostlist/1"

export default {
  name: "App",
  data() {
    return {
      postlist: [],
      userlist: [],
      perpagepost: 10,
      pagedpostlist: [],
    };
  },
  components: {
    Header: Header,
    Content: Content,
    Footer: Footer,
  },
  created() {
    axios({
      method: "GET",
      url: posturl,
    })
      .then((response) => {
        this.postlist = response.data;
        console.log(this.postlist);
      })
      .catch((response) => {
        console.log("Failed", response);
      });

    axios({
      method: "GET",
      url: userurl,
    })
      .then((response) => {
        this.userlist = response.data;
        console.log(this.userlist);
      })
      .catch((response) => {
        console.log("Failed", response);
      });
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Ubuntu:wght@500&display=swap");

#app {
  font-family: "Ubuntu", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.header {
  font-family: "Ubuntu", sans-serif;
}

.content {
  font-family: "Ubuntu", sans-serif;
}

.footer {
  font-family: "Ubuntu", sans-serif;
  background-color: #92caff;
  width: 100%;
  height: 60px;
  margin: 1% auto;
  text-align: center;
  box-shadow: 2px 2px 8px 2px rgb(167, 167, 167);
}
</style>
