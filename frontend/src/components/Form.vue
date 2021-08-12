<template>
  <div>
    <ckeditor v-model="postlist"></ckeditor>
  </div>
</template>

<script>

export default {
  name: 'Form',
  data(){
    return{

    }
  },
  props:{
    postlist: Array
  }
}
</script>

<style>

</style>