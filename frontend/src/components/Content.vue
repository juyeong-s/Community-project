<template>
    <div>  
       <div v-if="$store.state.step == 0">
           <router-link :to="{ name: 'PostForm'}" @click.native="changepage" class="link-form">✏</router-link>
           <div>
               <!-- Postlist Page -->
               <router-view :postlist="postlist" :userlist="userlist"/>
           </div>
       </div>
       
       <div v-if="$store.state.step == 1">
           <!-- Detail Page -->
           <PostDetail />
       </div>
       <div v-if="$store.state.step == 2">
           <!-- Form Page -->
           <PostForm :postlist="postlist"/>
       </div>
    </div>
</template>

<script>
import PostDetail from './PostDetail.vue'
// import PostList from './PostList.vue'
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
        Pagination
        // PostList,
        // Search
    },
    methods:{
        changepage(){
            store.commit("stepchange",{n: 2, item:null});
        },
        // postpage(page){
            
        // }
    },

};
</script>

<style>
.link-form{
    text-decoration: none;
}
</style>
