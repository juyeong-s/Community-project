<template>
    <header>
        <div class="header">
           <h1>VUE-COMMUNITY</h1>
        </div>
            <button class="back-btn" @click="$router.go(-1)">뒤로가기</button>
           <h3 class="content-header">게시판 리스트</h3>
               
           <div class="post-content">
               <ul class="post-head">
                   <li>제목</li>
                   <li>글쓴이</li>
                   <li>작성일</li>
               </ul>
           </div>
    </header>
</template>

<script>
export default {
    name: 'Header'
};
</script>

<style>
.header{
    text-align: center;
}
.back-btn{
    float: left;
}
.content-header {
    padding: 10px;
}
.post-content{
    text-align: center;
    background-color: aquamarine;
}
.post-head{
  list-style: none;
  display: inline-flex;
}
.post-head li {
  margin: 0 200px;
}
</style>