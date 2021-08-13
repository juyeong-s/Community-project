<template>
  <div>
        <label for="search">Search</label>
        <input v-model="serach" type="text" @input="searchkeyword" class="search-input">
  </div>

</template>

<script>
import EventBus from '../eventBus'

export default {
    name: 'Search',
    data:()=>{
        return {
            search: '',
            searchedData: []
        }
    },
    props:{
        postlist: Array
    },
    methods: {
        // handleSearchInput(e) { 
        //     this.postlist = e.target.value; 
        //     if(this.postlist.length !== 0){ 
        //         clearTimeout(this.debounce); 
        //         this.debounce = setTimeout(() => {
        //             const filteredList = this.stageInfoList.filter(item => 
        //             item.title.includes(this.postlist)); 
        //             this.searchList = filteredList; 
        //         }, 500); 
        //     }
        //     else{ 
        //         clearTimeout(this.debounce);
        //          this.debounce = setTimeout(() => { 
        //              this.searchList = []; 
        //         }, 500); 
        //     } 
        // },
        searchkeyword(e){
            this.searchedData = []
            this.search = e.target.value;
            console.log(this.search)
            this.postlist.forEach((post)=>{
                if([post.title, post.content].includes(this.search)){
                    this.searchedData.push(post)
                    console.log(this.searchedData)
                    EventBus.$emit('searchdata',this.searchedData);
                    // return searchedData
                }
            })
        }

    }
}
</script>

<style>
.search-input{
    border: 1px solid black;
}
</style>