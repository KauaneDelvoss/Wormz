<template>
  <div class="book-view">
    <v-container fluid class="container">
        <p>
            <span class="h3">{{ book.volumeInfo.title }}</span>
        </p>
        <p>
            <span class="subtitulo"> {{ book.volumeInfo.authors }}  </span>
            <span class="subtitulo"> {{ book.volumeInfo.publishedDate }} </span>
        </p>
        {{ id }}
    </v-container>
  </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
    layout: 'bib',
    data(){
        return{
            id: '',
            book: {}
        }
    },
    created(){
        this.id = this.$router.currentRoute.params.id
        this.$store.dispatch("book/GET_URL", this.id)
    },
    computed: {
        ...mapState('book', ['book'])
    }
}
</script>

<style>

</style>