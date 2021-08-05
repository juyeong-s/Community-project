<template>
  <div>
      바보
      <ul>
          <li>{{ posts.title }}</li>
          <li>{{ posts.content }}</li>
          <li>{{ posts.created_dt }}</li>
      </ul>
  </div>
</template>

<script>
export default {
    props: {
        posts: Object,
    }
}
</script>

<style>
ul{
    list-style: none;
    /* display: inline-flex; */
}
li {
    margin-right: 100px;
}

</style>
