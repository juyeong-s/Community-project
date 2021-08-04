<template>
    <div>
        <v-container fluid>
            <v-layout column>
                <div v-if="step == 2">
                    <h3 class="content-header">게시판 리스트</h3>
                
                    <div class="post-content">
                        <ul class="post-head">
                            <li>제목</li>
                            <li>글쓴이</li>
                            <li>작성일</li>
                        </ul>
                    </div>
                    <v-list-item v-for="(data, index) in propsdata" v-bind:key="index">
                        <router-view class="post-list" :data="data"></router-view>
                    </v-list-item>
                </div>

                <div v-else-if="step == 3">
                    <PostDetail />
                </div>

            <v-flex class="userList" column>
                    <v-card max-width="600" tile>
                        <v-list-item v-for="(data, index) in propsdata" v-bind:key="index">
                            <v-list-item-content>
                                <v-list-item-title>제목 {{ data.title }}</v-list-item-title>
                                <v-list-item-subtitle>내용 : {{ data.content }}</v-list-item-subtitle>
                            </v-list-item-content>
                        </v-list-item>
                    </v-card>
                </v-flex>

            </v-layout>
        </v-container>
    </div>
</template>

<script>
import PostDetail from './PostDetail.vue'
import PostList from './PostList.vue'
export default {
    name: 'Content',
    props:{
        step: Number,
        propsdata: Array
    },
    component:{
        PostDetail,
        PostList
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