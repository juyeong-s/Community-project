<template>
    <div>
    <h4>게시판 리스트</h4>
    <div class="post-content">
        <ul class="post-head">
          <li>글 제목</li>
          <li>글 내용</li>
          <li>작성일</li>
        </ul>
        <PostDetail />
    </div>
  </div>
</template>

<script>
import PostDetail from './PostDetail'

export default {
  name: 'PostList',
  components: {
    PostDetail
  }

}
</script>

<style>
.post-head{
  list-style: none;
  display: inline-flex;
}
.post-head li {
  margin-right: 100px;
}
</style>
