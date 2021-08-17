<template>
  <v-container fluid>
  <v-form>
      <v-text-field dense="dense" id="title" label="제목" 
       v-model="form.title" required></v-text-field>
       <v-text-field label="글쓴이(예비)" v-model="form.writer_fk_id"></v-text-field>
       <ckeditor
        tag-name="textarea"
        class="editor1"
        :v-model="editorData"
        name="editor1">
       </ckeditor>
      <router-link to="list/" class="mr-4" @click.native="submit">올리기</router-link>
  </v-form>
    <br>
  </v-container>
  
</template>

<script>
// import CKEditor from 'ckeditor4-vue';
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
        editorData: '<p>Content of the editor.</p>',
        // editorConfig:{
        //   toolbar: [ [ 'Bold' ] ]
        // },
      }
    },
    mounted(){
      // CKEDITOR.replace( 'editor1', {
      //   filebrowserBrowseUrl: '/browser/browse.php',
      //   filebrowserUploadUrl: '/uploader/upload.php'
      // });
    },
    props:{
      postlist: Array
    },
    // watch:{
    //   value(){
    //     let html = this.instance.getData()
    //     if (html !== this.value) {
    //       this.instance.setData(this.value)
    //       console.log(this.instance)
    //     }
    //   }
    // },
    methods: {
      submit(){
        if(this.form.title === ""){
          alert("제목을 입력해주세요");
          document.getElementById('title').focus();
          return false;
        }
        else{
          try{
            console.log(CKEDITOR.instances["editor1"])
            this.$form.content = CKEDITOR.instances.getData();
            htmlspecialchars(this.$form.content)
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
    // components:{
    //   ckeditor: CKEditor.component
    // },
}
</script>

<style>
/* .v-textarea{
    overflow-y: scroll;
    height: 400px;
} */
</style>