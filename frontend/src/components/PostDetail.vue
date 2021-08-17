<template>
  <div class="postdetail">
      <router-link :to="{ name: 'Pagination' }" class="back-btn" @click.native="stepchange(item)">목록으로</router-link>
      <table class="detail-table">
          <tbody>
              <tr class="detail-tr">
                    <th class="detail-th">제목</th>
              </tr>
              <hr>
              <tr class="detail-tr">
                    <td class="detail-td">{{ $route.params.item.title }}</td>
              </tr>
              <tr class="detail-tr">
                    <th class="detail-th">내용</th>                 
              </tr>
              <hr>
              <tr class="detail-tr">
                    <td class="detail-td" v-html="$route.params.item.content">{{ $route.params.item.content }}</td>
              </tr>
              <tr class="detail-tr">
                    <th class="detail-th">작성일</th>
              </tr>
              <hr>
              <tr class="detail-tr">
                    <td class="detail-td">{{ $route.params.item.created_dt }}</td>
              </tr>
          </tbody>
      </table>
  </div>
</template>

<script>
export default {
    name: 'PostDetail',
    props: {
        item: Object,
    },
    methods:{
        stepchange(){
            this.$store.commit("stepchange",{n: 0, item:null});
        }
    }
}

</script>

<style>
.postdetail{
    margin: 0 auto;
}
.detail-table{
    margin: 20px auto;
}
.detail-tr{
    padding: 50px 0px;
}
.detail-th{
    padding: 5px 0px;
}
.detail-td{
    padding: 0px 0 8px 0;
}
</style>
