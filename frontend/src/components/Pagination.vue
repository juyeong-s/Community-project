<template>
  <div class="overflow-auto">
      <b-table
      id="my-table"
      :items="postlist"
      :fields="fields"
      :per-page="perPage"
      :current-page="currentPage"
      :hover="true"
      small
    >
    <template v-slot:cell(title)="{ item }">
        <router-link :to="{name: 'PostDetail', params: { item: item }}" @click="toggleDetails(item)">
          {{item.title}}
        </router-link>
      </template>
    </b-table>
    <div class="mt-3">
      <b-pagination
      v-model="currentPage"
      :total-rows="rows"
      :per-page="perPage"
      pills
    ></b-pagination>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        pagedpostlist: [],
        perPage: 10,
        currentPage: 1,
        fields: [
            {
              key: 'id',
              label: '#',
            },
            {
              key: 'title',
              label: '제목',
            },
            {
              key: 'content',
              label: '내용',
            },
            {
              key: 'writer_fk_id',
              label: '글쓴이',
            },
            {
              key: 'created_dt',
              label: '작성일',
            },
        ]
      }
    },
    props:{
        postlist: Array
    },
    methods:{
        toggleDetails(item){
            if (item._showDetails) { // if details are open, close them
                item._showDetails = false
            } 
            else { // if details already exists, show the details
                this.$set(item, "_showDetails", true)
                console.log(item)
                // this.$store.commit('stepchange', {n:1, item: item})
            }
        },

    },
    computed: {
      rows() {
        console.log(this.postlist.length)
        return this.postlist.length
      }
    }
  }
</script>
