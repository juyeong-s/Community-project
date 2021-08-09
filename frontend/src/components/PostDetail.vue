<template>
  <div class="postdetail">
      <!-- {{$route.params.id}} -->
      <ul class="post-detail-ul">
          <li><strong>제목</strong><br>{{ post[$route.params.id].title }}</li>
          <li><strong>내용</strong><br> {{ post[$route.params.id].content }}</li>
          <li><strong>작성일</strong><br> {{ post[$route.params.id].created_dt }}</li>
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
.postdetail{
    margin: 0 auto;
}
.post-detail-ul{
    list-style: none;
    /* margin: 0 auto; */
}
.post-detail-ul li {
    margin: 50px 50px;
}

</style>
