<template>
<div class="post-list">
  <div v-for="(post,i) in postlist" :key="i">
    <ul>
      <li>
        <router-link :to="{ name: 'PostDetail', params: { id: i, post: postlist }}">
          {{ post.title }}
        </router-link>
      </li>
      <li>{{ postlist[i].content }}</li>
      <li>{{ postlist[i].writer_fk_id }}</li>
      <li>{{ $moment(postlist[i].created_dt).format('YYYY-MM-DD hh:mm') }}</li>
    </ul>
    </div>
   </div>
</template>

<script>

export default {
  name: 'PostList',
  props:{
    postlist : Array
  },

}
</script>

<style>
.post-list{
  width: 100%;
  height: 500px;
  background-color: rgb(208, 208, 255);
}
ul{
  list-style: none;
  display: flex;
}
li{
  margin: 0 auto;
}

</style>
