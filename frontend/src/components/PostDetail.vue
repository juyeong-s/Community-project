<template>
  <div class="post-list">
      <ul class="post-item">
          <li>{{ post.title }}</li>
          <li>{{ post.content }}</li>
          <li>{{ post.created_dt }}</li>
      </ul>
  </div>
</template>

<script>
export default {
    props: {
        post: Object,
        index: Number
    }
}
</script>

<style>
.post-item{
    list-style: none;
    /* display: inline-flex; */
}
.post-item li {
    margin-right: 100px;
}

</style>
