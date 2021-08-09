<template>
    <div>  
       <div v-if="$store.state.step == 0">
           <router-link :to="{ name: 'PostForm'}" @click.native="changepage"><v-icon>mdi-pencil</v-icon></router-link>
           <div>
               <router-view :postlist="postlist" :userlist="userlist"/>
           </div>
           <div class="text-center">
                <Pagination />
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
import Pagination from './Pagination.vue'
import store from '../store';

export default {
    name: 'Content',
    props:{
        postlist: Array,
        userlist: Array
    },
    components:{
        PostForm,
        PostDetail,
        PostList,
        Pagination
    },
    methods:{
        changepage(){
            store.commit("stepchange",2);
        }
    },

};
</script>

<style>

</style>
