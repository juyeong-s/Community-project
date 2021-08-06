<template>
    <div>
        <router-link to="form/" @click="$store.commit('stepchange',2)"><v-icon>mdi-pencil</v-icon></router-link>
       <div v-if="$store.state.step == 0">
           <div>
               <router-view :postlist="postlist" />
           </div>
       </div>
       
       <div v-if="$store.state.step == 1">
           <router-view />
       </div>
       <div v-if="$store.state.step == 2">
           <PostForm :postlist="postlist"/>
       </div>
    </div>
</template>

<script>
import PostDetail from './PostDetail.vue'
import PostList from './PostList.vue'
import PostForm from './PostForm.vue'

export default {
    name: 'Content',
    props:{
        postlist: Array
    },
    components:{
        PostForm,
        PostDetail,
        PostList,
    }
};
</script>

<style>

</style>
