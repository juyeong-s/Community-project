<template>
<div class="post-list">
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
  <div class="pagination">
    <b-pagination
      v-model="currentPage"
      :total-rows="rows"
      :per-page="perPage"
      aria-controls="my-table"
      @page-click="pageClick"
    ></b-pagination>
  </div>  
  </div>
</template>

<script>

export default {
  name: 'PostList',
  data(){
    return {
      perPage: 10,
      currentPage: 0,
    }
  },
  props:{
    postlist : Array,
    userlist: Array
  },
  methods:{
    pageClick: ()=>{
			this.currentPage += 1;
      this.$emit("postpage",this.currentPage)
			// this.getNoticeListByPage(page);
		},
    // getNoticeListByPage: function (page) {
    //   var limit = 20;
    //   var offset = (page - 1) * limit;
    //   this.loading = true;
    //   this.$http
    //       .get('http://127.0.0.1:8000/community/getPostlist/' + `?offset=${offset}&limit=${limit}`)
    //       .then(response => {
    //           this.items = response.data;
    //       })
    //       .catch(error => {
    //           console.log(error);
    //       })
    //       .finally(() => this.loading = false);
		// 	}
  },
  computed: {
      rows() {
        return this.postlist.length
      },
      paginatedData () {
      const start = this.currentPage,
            end = start + this.perPage;
      return this.postlist.slice(start, end);
    }
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

</style>
