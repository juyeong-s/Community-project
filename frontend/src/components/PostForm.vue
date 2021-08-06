<template>
  <v-container fluid>
<v-form>
    <v-text-field dense="dense" label="제목" 
     v-model="form.title" required></v-text-field>
     <v-text-field label="글쓴이(예비)" v-model="form.writer_fk_id"></v-text-field>
    <v-textarea
        name="input-7-1"
        filled="filled"
        label="내용"
        auto-grow="auto-grow"
        style="overflow-y: scroll"
        height="400"
        v-model="form.content"></v-textarea>
    <v-btn class="mr-4" @click="submit">올리기</v-btn>
    </v-form>
  </v-container>
  
</template>

<script>
import axios from "axios"
let url = "http://127.0.0.1:8000/community/postsave/"

export default {
    name: 'PostForm',
    data: ()=>{
      return {
        form: {
          title: '',
          writer_fk_id: 0,
          content: '',
        }
      }
    },
    props:{
      postlist: Array
    },
    methods: {
      submit(){
        // this.$store.commit('changestep',1)
        console.log(this.form)
        axios.post(url,this.form)
        .then((res)=>{
          console.log(res);
        })
        .catch((error)=>{
          console.log("err", error.response)
        });

      }
    }

}
</script>

<style>
/* .v-textarea{
    overflow-y: scroll;
    height: 400px;
} */

</style>