<template>
  <v-container fluid>
    <router-link :to="{ name: 'Pagination' }" class="back-btn" @click.native="stepchange">목록으로</router-link>
  <v-form>
      <v-text-field dense="dense" id="title" label="제목" 
       v-model="form.title" required></v-text-field>
       <v-text-field label="글쓴이(예비)" v-model="form.writer_fk_id"></v-text-field>
       <ckeditor
       tag_name="textarea"
        id="content"
        :v-model="form.content"
        @change="contentsave($event.target.value)"
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
        content_info: null,
        // editdata:this.$route.query,
        editorData: '',
        // editorConfig:{
        //   toolbar: [ [ 'Bold' ] ]
        // },
      }
    },
    mounted(){

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
      stepchange(){
        this.$store.commit("stepchange",{n: 0, item:null});
      },
      submit(){
        if(this.form.title === ""){
          alert("제목을 입력해주세요");
          document.getElementById('title').focus();
          return false;
        }
        else{
          this.content_info = this.contentsave()
          console.log("content_info",this.content_info)
          try{
            // console.log(this.form.content)
            // console.log(CKEDITOR.instances['content'])
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
      },
      contentsave(e){
        return e;
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