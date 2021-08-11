<template>
  <div class="postdetail">
      <router-link :to="{ name: 'Pagination' }" class="back-btn">목록으로</router-link>
        <ul class="post-detail-ul">
            <li><strong>제목</strong><br>{{ item.title }}</li>
            <li><strong>내용</strong><br> {{ item.content }}</li>
            <li><strong>작성일</strong><br> {{ item.created_dt }}</li>
      </ul>
  </div>
</template>

<script>
export default {
    name: 'PostDetail',
    props: {
        item: Object,
    },
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

// <li><strong>내용</strong><br> {{ post[$route.params.id].content }}</li>
//           <li><strong>작성일</strong><br> {{ post[$route.params.id].created_dt }}</li>
