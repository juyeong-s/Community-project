<template>
  <v-container fluid>
  <v-form>
      <v-text-field dense="dense" id="title" label="제목" 
       v-model="form.title" required></v-text-field>
       <v-text-field label="글쓴이(예비)" v-model="form.writer_fk_id"></v-text-field>
       <ckeditor
        id="content"
        :v-model="form.content"
        name="editor1">
       </ckeditor>
      <router-link to="list/" class="mr-4" @click.native="submit">올리기</router-link>
  </v-form>
    <br>
  </v-container>
  
</template>

<script>
import CKEditor from 'ckeditor4-vue';
import axios from "axios"
let url = "http://127.0.0.1:8000/community/postsave/"
// const upload = require('../assets/upload')
export default {
    name: 'PostForm',
    data: ()=>{
      return {
        form: {
          title: '',
          writer_fk_id: 0,
          content: '',
        },
        editorData: '',
        // editorConfig:{
        //   toolbar: [ [ 'Bold' ] ]
        // },
      }
    },
    updated(){
      CKEDITOR.replace( 'editor1', {
        filebrowserBrowseUrl: '/browser/browse.php',
        filebrowserUploadUrl: '/uploader/upload.php'
      });
    },
    props:{
      postlist: Array
    },
    watch:{
      value: function(){
        this.form.content = this.value;
      }
    },
    methods: {
      submit(){
        if(this.form.title === ""){
          alert("제목을 입력해주세요");
          document.getElementById('title').focus();
          return false;
        }
        else{
          try{
            console.log(this.form.content)
            console.log(CKEDITOR.instances['content'])
            // this.form.content = CKEDITOR.instances['content']['_'].getData();
            // htmlspecialchars(this.form.content)
            this.$store.commit('stepchange',{n: 0, item:null})
            console.log(this.form)
            axios.post(url,this.form)
            .then((res)=>{
              console.log(res);
            })
            .catch((error)=>{
              console.log("err", error.response)
            });
          }
          catch(error){
            console.log(error);
          }
        }
      }
    },
    components:{
      ckeditor: CKEditor.component
    },
}
</script>

<style>
/* .v-textarea{
    overflow-y: scroll;
    height: 400px;
} */
</style>