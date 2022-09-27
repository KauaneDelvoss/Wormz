<template>
  <div class="bookshelf-view">
    {{ id }}
    <v-row class="d-flex justify-center row">
      <div v-for="book in this.bookshelf" :key="book" class="my-2 mx-5">
        <CardBooks :book="book" />
      </div>
    </v-row>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
    layout: 'bib',
    data(){
        return{
            id: 0
        }
    },
    mounted() {
        this.$store.dispatch("bib/GET_URL")
        this.id = this.$router.currentRoute.params.id
    },
    computed: {
      ...mapState('bib', ['bookshelf'])
    }
}
</script>

<style scoped lang="scss">
</style>