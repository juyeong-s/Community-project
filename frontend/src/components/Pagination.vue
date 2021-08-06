<template>
  <div class="pagination text-center">
    <v-pagination
      v-model="page"
      :length="15"
      :total-visible="7"
    ></v-pagination>
  </div>
</template>

<script>
  export default {
    name: 'Pagination',
    data () {
      return {
        page: 1,
      }
    },
  }
</script>

<style>
.pagination{
    width: 500px;
    margin: 0 auto;
}
</style>