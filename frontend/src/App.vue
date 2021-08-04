<template>
  <div>
      <Header class="header" :step="step"></Header>
      <Content class="content" :step="step" :propsdata="dataList"></Content>
      <Footer class="footer" :step="step"></Footer>
    </div>
</template>

<script>
import axios from "axios"
// import PostList from './components/PostList.vue'
import Header from "./components/Header.vue"
import Content from "./components/Content.vue"
import Footer from "./components/Footer.vue"
let url = "http://127.0.0.1:8000/community/getlist/";

export default {
  name: 'App',
  data(){
      return{
        step: 2,
        dataList : []
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
      url: url 
    })
    .then(response => {
      this.dataList = response.data;
      console.log(this.dataList)
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
// export default {
//   name: 'App',
//   data(){
//     return {
//       userList : []
//     }
//   },
//   components: {
//     header: Header,
//     content: Content,
//     footer: Footer,
//   },
//   methods: {
//     getData(){
//       axios.get("http://127.0.0.1:8000/community/post/")
//       .then((res)=>{
//         for(let i of res.data){
//           this.userList.push({
//             id: i.pk,
//             title: i.fields.title,
//             writer_fk_id: i,
//             content: i.fields.content,
//             created_dt: i.fields.created_dt,
//             modified: i.fields.modified
//           })
//         }
//       })
//       .catch((err)=>{
//         alert(err);
// })
//     }
//   }
// }

<style>
#app {
  font-family: 'Do Hyeon', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.header{
  text-align: center;
}
.content{
  background-color: #d1f6ff
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
