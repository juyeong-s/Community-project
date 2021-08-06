<template>
  <div>
      {{$route.params.id}}
      <ul>
          <li>{{ post[$route.params.id].title }}</li>
          <li>{{ post[$route.params.id].content }}</li>
          <li>{{ post[$route.params.id].created_dt }}</li>
      </ul>
  </div>
</template>

<script>
export default {
    name: 'PostDetail',
    props: {
        post: Array,
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
