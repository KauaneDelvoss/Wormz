<template>
  <div class="bookshelf-view">
    {{ id }}
  </div>
</template>

<script>
export default {
    layout: 'bib',
    data(){
        return{
            id: 0
        }
    },
    mounted() {
        this.id = this.$router.currentRoute.params.id
    }
}
</script>

<style>

</style>