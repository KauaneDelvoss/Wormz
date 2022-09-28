<template>
  <div class="book-view">
        <v-row v-if="book.volumeInfo" class="d-flex container">
            <v-col cols="6">
                <div>
                    <p>
                        <span class="h3">{{ book.volumeInfo.title }}</span>
                    </p>
                </div>
                <div>
                    <div v-for="author in book.volumeInfo.authors" :key="author">
                        <span class="subtitulo"> {{ author }} </span>
                    </div>
                    <span class="subtitulo data"> {{ book.volumeInfo.publishedDate }} </span>
                </div>
            </v-col>
            <v-col cols="6" class="d-flex justify-end">
                <v-card class="mx-auto book">
                    <v-img
                    v-if="
                        book.volumeInfo.imageLinks
                        ? book.volumeInfo.imageLinks.thumbnail
                        : false
                    "
                    :src="book.volumeInfo.imageLinks.thumbnail"
                    height="28vh"
                    aspect-ratio="1.7"
                    />
                </v-card>
            </v-col>
        </v-row>
  </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
    layout: 'bib',
    data(){
        return{}
    },
    mounted(){
        const id = this.$router.currentRoute.params.id
        this.$store.dispatch("book/GET_URL", id)
        console.log(this.book)
    },
    computed: {
        ...mapState('book', ['book'])
    }
}
</script>

<style scoped lang="scss">
.data{
    font-size: 1.5vw;
    opacity: 80%;
}

.book{
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    background-color: variables.$primary-color;
    border-radius: 15px;
    height: 10vw;
    width: 9vw
}
</style>