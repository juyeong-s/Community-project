<template>
  <div class="overflow-auto">
  <div>
    <label for="search">Search</label>
    <input v-model="search" type="text" @input="searchkeyword($event.target.value)" class="search-input" placeholder="🔍">
  </div>
      <b-table
      id="my-table"
      :items="searchedData"
      :fields="fields"
      :per-page="perPage"
      :current-page="currentPage"
      :hover="true"
      small
    >
    <template v-slot:cell(title)="{ item }">
        <router-link :to="{name: 'PostDetail', params: { item: item }}" @click.native="viewCountIncre(item)"
        class="title-link">
          <b>{{item.title}}</b>
        </router-link>
      </template>
    </b-table>
    <div class="mt-3">
      <b-pagination
      v-model="currentPage"
      :total-rows="rows"
      :per-page="perPage"
      pills
    ></b-pagination>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        perPage: 10,
        currentPage: 1,
        search: "",
        searchedData: [...this.postlist],
        count: 0,
        fields: [
            {
              key: 'id',
              label: '#',
            },
            {
              key: 'title',
              label: '제목',
            },
            {
              key: 'content',
              label: '내용',
            },
            {
              key: 'writer_fk_id',
              label: '글쓴이',
            },
            {
              key: 'view_cnt',
              label: '조회수',
            },
            {
              key: 'created_dt',
              label: '작성일',
            },
        ]
      }
    },
    props:{
        postlist: Array
    },
    methods:{
      // 조회수 함수
        viewCountIncre(item){
          console.log("viewCountIncre실행됨",item)
          item.view_cnt += 1;
        },
        // 검색함수
        searchkeyword(e){
          this.searchedData = [...this.postlist]
          this.search = e;
          console.log(this.searchedData)
          console.log(this.search)
          for(let i=0; i<this.searchedData.length; i++){
            if(!this.searchedData[i].title.includes(this.search)){
              this.searchedData.splice(i,1);
              i--;
            }
          }
          if(this.searchedData.length === this.postlist.length){
            this.searchedData = [...this.postlist]
          }
          console.log("searchedData",this.searchedData)
        }

    },
    computed: {
      // 전체 게시물 개수
      rows() {
        console.log("this.postlist.length",this.postlist.length)
        return this.postlist.length
      },
    },
    // 원본 복제
    updated(){
        if(this.count === 0){
          this.searchedData = [...this.postlist]
          this.count+=1
        }
        console.log("searchedData함수",this.searchedData)
        console.log("count",this.count)
        return this.searchedData
    }
  }
</script>
<style scoped>
.search-input{
    border: 1px solid black;
}
.title-link{
  color: black;
  text-decoration: none;
}
</style>
