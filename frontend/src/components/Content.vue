<template>
    <div>
        <v-container fluid>
            <v-layout column>
                <div v-if="step == 0">
                    <h3 class="content-header">게시판 리스트</h3>         
                    <v-btn
                        class="ma-2"
                        outlined
                        large
                        fab
                        color="teal"
                        @click="$store.commit('stepchange',2)"
                    >
                        <v-icon>mdi-pencil</v-icon>
                    </v-btn>
                    <div class="post-content">
                        <ul class="post-head">
                            <li>제목</li>
                            <li>글쓴이</li>
                            <li>작성일</li>
                        </ul>
                    </div>
                        <PostList class="post-list" :postlist="postlist" :step="step"></PostList>
                </div>

                <div v-else-if="step == 1">
                    <PostDetail />
                </div>

                <div v-else-if="step == 2">
                    <PostForm />
                </div>

            </v-layout>
        </v-container>
    </div>
</template>

<script>
import PostDetail from './PostDetail.vue'
import PostList from './PostList.vue'
import PostForm from './PostForm.vue'
export default {
    name: 'Content',
    props:{
        step: Number,
        postlist: Array
    },
    component:{
        PostDetail,
        PostList,
        PostForm
    }
};
</script>

<style>
.content-header {
    padding: 10px;
    text-align: center;
}
.post-content{
    text-align: center;
}
.post-head{
  list-style: none;
  display: inline-flex;
}
.post-head li {
  margin: 0 200px;
}
.post-list{
    width: 100%;
    background-color: rgb(152, 136, 243);
}

</style>
