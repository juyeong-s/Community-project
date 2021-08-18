<template>
  <v-container fluid>
    <router-link :to="{ name: 'Pagination' }" class="back-btn" @click.native="stepchange">목록으로</router-link>
  <form id="PostSaveForm" name="PostSaveForm" enctype="multipart/form-data">
      <v-text-field dense="dense" id="title" label="제목" 
       v-model="form.title" required></v-text-field>
       <v-text-field label="글쓴이(예비)" v-model="form.writer_fk_id"></v-text-field>
       
       <ckeditor
       tag_name="textarea"
        id="ckcontent"
        :v-model="form.content"
        @input="contentsave($event.target.value)"
        name="ckcontent">
       </ckeditor>

      <button type="submit"><router-link to="list/" class="mr-4" @click.native="submit">올리기</router-link></button>
  </form>
    <br>
  </v-container>
  
</template>

<script>
import CKEditor from 'ckeditor4-vue';
import axios from "axios"
let url = "http://127.0.0.1:8000/community/postsave/"
// const upload = require('../assets/upload')
// CKEDITOR.replace( 'ckcontent', {
//         // toolbar:
//         // [['Bold','-','italic']],
//         uiColor: '#dcdcdc',
//         content: '',
//         filebrowserBrowseUrl: 'http://127.0.0.1:8000/community/uploadImg/1',
//         filebrowserUploadUrl: 'http://127.0.0.1:8000/community/uploadImg/1'
//       });
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
    updated(){
      CKEDITOR.replace( 'ckcontent', {
        // toolbar:
        // [['Bold','-','italic']],
        content: this.form.content,
        uiColor: '#dcdcdc',
        filebrowserBrowseUrl: 'http://127.0.0.1:8000/community/uploadImg/1',
        filebrowserUploadUrl: 'http://127.0.0.1:8000/community/uploadImg/1'
      });
    },
    mounted(){
      // console.log(this.$route.query.forms)
      this.form.title = this.$route.query.forms.title;
      this.form.content = this.$route.query.forms.content;
      this.form.writer_fk_id = this.$route.query.forms.writer_fk_id;
      // CKEDITOR.instances["ckcontent"].setData('<p>'+this.form.content+'</p>');
      console.log(this.form.content)
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
          try{
            for(let instance in CKEDITOR.instances){
              CKEDITOR.instances[instance].updateElement();
              this.form.content = CKEDITOR.instances[instance].getData();
              console.log("form.content", this.form.content)
            }
            this.$store.commit('stepchange',{n: 0, item:null})
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