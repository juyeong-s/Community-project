<template>
  <v-container fluid>
    <router-link
      :to="{ name: 'Pagination' }"
      class="back-btn"
      @click.native="stepchange"
      >목록으로</router-link
    >
    <form id="PostSaveForm" name="PostSaveForm" enctype="multipart/form-data">
      <v-text-field
        dense="dense"
        id="title"
        label="제목"
        v-model="form.title"
        required
      ></v-text-field>
      <v-text-field
        label="글쓴이(예비)"
        v-model="form.writer_fk_id"
      ></v-text-field>

      <ckeditor
        :editor="editor"
        id="ckcontent"
        :v-model="editorData"
        name="ckcontent"
      >
      </ckeditor>

      <button type="submit">
        <router-link to="list/" class="mr-4" @click.native="submit"
          >올리기</router-link
        >
      </button>
    </form>
    <br />
  </v-container>
</template>

<script>
// import CKEditor from 'ckeditor4-vue';
import ClassicEditor from "@ckeditor/ckeditor5-editor-classic/src/classiceditor";
// import EssentialsPlugin from "@ckeditor/ckeditor5-essentials/src/essentials";
// import Bold from "@ckeditor/ckeditor5-basic-styles/src/bold";
// import ItalicPlugin from "@ckeditor/ckeditor5-basic-styles/src/italic";
// import LinkPlugin from "@ckeditor/ckeditor5-link/src/link";
// import ParagraphPlugin from "@ckeditor/ckeditor5-paragraph/src/paragraph";
import CKEditor from "@ckeditor/ckeditor5-vue2";
// import CKEditor from '@ckeditor/ckeditor5-vue'
// import ClassicEditor from '@ckeditor/ckeditor5-editor-classic/src/classiceditor';
// import CKFinder from '@ckeditor/ckeditor5-ckfinder/src/ckfinder';
import axios from "axios";
let url = "http://127.0.0.1:8000/community/postsave/";
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
  name: "PostForm",
  data: () => {
    return {
      editor: ClassicEditor,
      form: {
        id: 0,
        title: "",
        writer_fk_id: 0,
        content: "",
      },
      editorData: "",
      // editorConfig:{
      //   toolbar: [ [ 'Bold' ] ]
      // },
    };
  },
  updated() {
    CKEDITOR.replace("ckcontent", {
      // toolbar:
      // [['Bold','-','italic']],
      content: this.form.content,
      uiColor: "#dcdcdc",
      filebrowserBrowseUrl: "http://127.0.0.1:8000/community/uploadImg/1",
      filebrowserUploadUrl: "http://127.0.0.1:8000/community/uploadImg/1",
    });
  },
  mounted() {
    // 수정을 위한
    this.form.id = this.$route.query.forms.id;
    this.form.title = this.$route.query.forms.title;
    this.form.content = this.$route.query.forms.content;
    this.form.writer_fk_id = this.$route.query.forms.writer_fk_id;
    console.log(this.form.content);
  },
  props: {
    postlist: Array,
  },
  // watch:{
  //   value: function(){
  //     this.form.content = this.value;
  //   }
  // },
  methods: {
    stepchange() {
      this.$store.commit("stepchange", { n: 0, item: null });
    },
    submit() {
      if (this.form.title === "") {
        alert("제목을 입력해주세요");
        document.getElementById("title").focus();
        return false;
      } else {
        try {
          for (let instance in CKEDITOR.instances) {
            CKEDITOR.instances[instance].updateElement();
            this.form.content = CKEDITOR.instances[instance].getData();
            console.log("form.content", this.form.content);
          }
          this.$store.commit("stepchange", { n: 0, item: null });
          axios
            .post(url, this.form)
            .then((res) => {
              console.log(res);
            })
            .catch((error) => {
              console.log("err", error.response);
            });
        } catch (error) {
          console.log(error);
        }
      }
    },
  },
  components: {
    ckeditor: CKEditor.component,
  },
};
</script>

<style>
/* .v-textarea{
    overflow-y: scroll;
    height: 400px;
} */
ckeditor {
  background-color: blue;
}
</style>
