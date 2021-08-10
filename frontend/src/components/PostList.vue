<template>
<div class="post-list">
  {{pagedpostlist}}
  <table>
  <tbody>
    <tr v-for="(post,i) in paginatedData.slice().reverse()" :key="i">
      <td>
        {{i+1}}
      </td>
      <td>
        <router-link :to="{ name: 'PostDetail', params: { id: postlist.length - i-1, post: postlist }}">
          {{ post.title }}
        </router-link>
      </td>
      <td>{{ post.content }}</td>
      <td>{{ userlist[postlist.length - i-1] }}</td>
      <td>{{ post.view_cnt }}</td>
      <td>{{ $moment(post.created_dt).format('YYYY-MM-DD hh:mm') }}</td>
    </tr>
  </tbody>
  </table>
  <Pagination :postlist="postlist"/>
 
  </div>
</template>

<script>
import Pagination from './Pagination.vue'

export default {
  name: 'PostList',
  data(){
    return {
      perPage: 10,
      currentPage: 1,
      pagedpostlist: []
    }
  },
  props:{
    postlist : Array,
    userlist: Array
  },
  methods:{
    prevpage(){
      this.$store.commit('prevpage',1)
    },
    nextpage(){
      this.$store.commit('nextpage',1)
    },
    gopage(num){
      this.$store.commit('gopage',num)
      let currpage = this.$store.state.currentPage;
      console.log("list-현재페이지",currpage)
      // let pagedposturl = "http://127.0.0.1:8000/community/pagedpostlist/"+currpage;
      console.log(Math.ceil(this.postlist.length/this.perPage))
      // for(; currpage<=Math.ceil(this.postlist.length/this.perPage); currpage++){
          let pagedposturl = "http://127.0.0.1:8000/community/pagedpostlist/"+num;
          console.log("for문 들어옴")
          axios({
            method: "GET",
            url: pagedposturl 
          })
          .then(response => {
            this.pagedpostlist = response.data;
            console.log(this.pagedpostlist) 
          })
          .catch(response => {
            console.log("Failed", response);
          });
      // }
    }
  },
  computed: {
      rows() {
        this.$store.commit('allpagenum',Math.ceil(this.postlist.length/this.perPage))
        return this.$store.state.pageNum
      },
      pagenum(){
        return Math.ceil(this.postlist.length/this.perPage);
      },
      paginatedData () {
      const start = this.currentPage,
            end = start + this.perPage;
      return this.postlist.slice(start, end);
    }
    },
    components:{
      Pagination
    }
}
</script>

<style>
.pagination{
  margin: 80px auto;
}
.post-list{
  width: 100%;
  height: 500px;
  background-color: rgb(208, 208, 255);
}
.post-list-ul{
  list-style: none;
  display: flex;
}
.post-list-ul li{
  margin: 0 auto;
}
.prevbtn{
  width: 40px;
  border: 1px solid rgb(114, 114, 114);
  color: rgb(114, 114, 114);
  background-color: rgb(226, 255, 240);
  border-radius: 5px;
}
.nextbtn{
  width: 40px;
  border: 1px solid rgb(114, 114, 114);
  color: rgb(114, 114, 114);
  background-color: rgb(226, 255, 240);
  border-radius: 5px;
}
.numbtn{
  width: 40px;
  border: 1px solid rgb(114, 114, 114);
  color: rgb(114, 114, 114);
  background-color: rgb(226, 255, 240);
  border-radius: 5px;
}
</style>

    // <b-pagination
    //   v-model="currentPage"
    //   :total-rows="rows"
    //   :per-page="perPage"
    //   aria-controls="my-table"
    //   @page-click="this.$store.commit('changepage', this.currentPage)"
    // ></b-pagination>

  //     <div class="pagination">
  //   <router-link :to="{ name: 'PostList', params: { id: currentPage }}">
  //     <button @click="prevpage" class="prevbtn">이전</button>
  //     <button v-for=" num in rows" :key="num" @click="gopage(num)" class="numbtn">{{num}}</button>
  //     <button @click="nextpage" class="nextbtn">다음</button>
  //   </router-link>
  // </div> 