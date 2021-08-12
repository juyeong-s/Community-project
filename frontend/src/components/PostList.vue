<template>
<div class="post-list">
  <div>
    <label for="search">Search</label>
    <input v-model="serach" type="text" @input="searchkeyword($event.target.value)" class="search-input" placeholder="🔍">
  </div>
  <table>
  <tbody>
    <tr v-for="(post,i) in paginatedData.slice().reverse()" :key="i">
      <td class="post-title">
        {{i+1}}
      </td>
      <td>
        <router-link :to="{ name: 'PostDetail', params: { id: postlist.length - i-1, post: postlist }}">
          {{ post.title }}
        </router-link>
      </td>
      <td class="post-content"><code>{{ displaycontent }}</code></td>
      <td class="post-writer">{{ userlist[postlist.length - i-1] }}</td>
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
import PostForm from './PostForm.vue'

export default {
  name: 'PostList',
  data(){
    return {
      perPage: 10,
      currentPage: 1,
      pagedpostlist: [],
      search: '',
      searchedData: []
    }
  },
  props:{
    postlist : Array,
    userlist: Array
  },
  methods:{
    searchkeyword(e){
      this.searchedData = [...this.postlist]
      this.search = e.target.value;
      console.log(this.search)
      for(let i=0; i<this.searchedData.length; i++){
        if(![this.searchedData[i].title].includes(this.search)){
          this.searchedData.splice(i,1);
          i--;
        }
      }
      console.log(this.searchedData)
    },
    displaycontent(){
      return CKEditor.instances.editor1.getData()
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
      Pagination,
      PostForm
    },
}
</script>

<style>
.container{
  background-color: aliceblue;
}
.search-input{
    border: 1px solid black;
}
.pagination{
  margin: 80px auto;
}
.post-list{
  width: 100%;
  height: 500px;
  background-color: rgb(208, 208, 255);
}
.post-title{
  color: dimgray;
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

  //   <div>
  //   <label for="search">Search</label>
  //   <input v-model="serach" type="text" @input="searchkeyword" class="search-input">
  // </div>