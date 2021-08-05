<template>
  <div class="post-head" :v-for="(post, i) in postlist" :key="i">
    <ul>
      <li><router-link :to="{ name: 'PostDetail', params: { id: i }}" :post="post">{{ post[i].title }}</router-link></li>
      <li>{{ post[i].content }}</li>
      <li>{{ post[i].created_dt }}</li>
    </ul>
   </div>
</template>

<script>

export default {
  name: 'PostList',
  data: () => ({
    }),
  props:{
    postlist : Array,
    step: Number
  },
  components: {
  },
  methods:{
    // Showpost(post){
    //   $router.push({path: "/detail"+this.index, post})
    // }
  }

}
</script>

<style>
.post-head{
  width: 100%;
  
}
.ul{
  list-style: none;
  display: inline-flex;
}
v-card{
  text-align: center;
}
v-list-item {
  margin: 0 auto;
}


</style>

//

//     <div class="post-content">
//         <v-list-card class="post-head">
//           <v-list-item><router-link to="/detail/index" @click="step++">{{ post.title }}</router-link></v-list-item>
//           <v-list-item>{{ post.content }}</v-list-item>
//           <v-list-item>{{ post.created_dt }}</v-list-item>
//         </v-list-card>
//     </div>
//

    // <v-flex class="userList" column>
    //          <v-card max-width="600" tile>
    //              <v-list-item v-for="(post, index) in postlist" v-bind:key="index">
    //                  <v-list-item-content>
    //                      <v-list-item-title>제목 : {{ post.title }}</v-list-item-title>
    //                      <v-list-item-subtitle>내용 : {{ post.content }}</v-list-item-subtitle><br>
    //                  </v-list-item-content>
    //              </v-list-item>
    //          </v-card>
    //      </v-flex>