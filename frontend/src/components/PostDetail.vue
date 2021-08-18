<template>
  <div class="postdetail">
      <router-link :to="{ name: 'Pagination' }" class="back-btn" @click.native="stepchange">목록으로</router-link>
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
      <button @click="editPost">수정</button>
      <button @click="deletePost">삭제</button>
  </div>
</template>

<script>
import axios from "axios"
export default {
    name: 'PostDetail',
    props: {
        item: Object,
        form: {
          title: '',
          writer_fk_id: 0,
          content: '',
          created_dt: ''
        },
    },
    methods:{
        stepchange(){
            this.$store.commit("stepchange",{n: 0, item:null});
        },
        editPost(){
            const forms = this.$route.params.item;
            this.$store.commit("stepchange",{n: 2, item:forms});
            console.log(forms)
            this.$router.push({name: 'PostForm', query: {forms: forms} });
        },
        deletePost(){
            if(confirm("삭제하시겠습니까?")){
                axios.delete('http://127.0.0.1:8000/community/postdelete/'+this.$route.params.item.id)
                .then((res)=>{
                    console.log(res);
                    if(res){
                        alert("삭제되었습니다.");
                        this.$store.commit("stepchange",{n: 0, item:null});
                        this.$router.push({path: 'list/', query: this.$route.params.item});       
                    }
                    else{
                        alert("삭제에 실패했습니다. 다시 시도해주세요.");
                    }
                })
                .catch((err)=>{
                    console.log(err);
                })
            }
        }
    },
    // mounted(){
    //     console.log(this.$route.params.item)
    //     this.form.title = this.$route.params.item.title;
    //     this.form.content = this.$route.params.item.content;
    //     this.form.writer_fk_id = this.$route.params.item.writer_fk_id;
    //     this.form.created_dt = this.$route.params.item.created_dt;
    //     console.log(this.form)
    // }
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
