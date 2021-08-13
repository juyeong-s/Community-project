<template>
  <v-container fluid>
<v-form>
    <v-text-field dense="dense" id="title" label="제목" 
     v-model="form.title" required></v-text-field>
     <v-text-field label="글쓴이(예비)" v-model="form.writer_fk_id"></v-text-field>
     <ckeditor id="editor1" :value="value" name="editor1"></ckeditor>
    <router-link to="list/" class="mr-4" @click.native="submit">올리기</router-link>
    </v-form>
    <br>
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
        },
        instance: null
      }
    },
    props:{
      postlist: Array
    },
    watch:{
      value(){
        let html = this.instance.getData()
        if (html !== this.value) {
          this.instance.setData(this.value)
          console.log(this.instance)
        }
      }
    },
    methods: {
      submit(){
        if(this.form.title === ""){
          alert("제목을 입력해주세요");
          document.getElementById('title').focus();
          return false;
        }
        this.$form.content = CKEDITOR.instances["#editor1"].getData();
        htmlspecialchars(this.$form.content)
        this.$store.commit('stepchange',{n: 0, item:null})
        // console.log(this.form)
        axios.post(url,this.form)
        .then((res)=>{
          console.log(res);
        })
        .catch((error)=>{
          console.log("err", error.response)
        });

      }
    },
    components:{

    },
}
</script>

<style>
/* .v-textarea{
    overflow-y: scroll;
    height: 400px;
} */

</style>