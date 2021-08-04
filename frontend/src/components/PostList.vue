<template>
    <div class="post-content">
        <ul class="post-head">
          <li><router-link to="/detail/index">{{ data.title }}</router-link></li>
          <li>{{ data.content }}</li>
          <li>{{ data.created_dt }}</li>
        </ul>
    </div>
</template>

<script>

export default {
  name: 'PostList',
  props:{
    data : Array
  },
  components: {
  },
  methods:{
    Showpost(){

    }
  }

}
</script>

<style>
/* .post-content{
  width: 100%;
} */
.post-head{
  list-style: none;
  display: inline-flex;
}
.post-head li {
  margin-right: 100px;
}
</style>
