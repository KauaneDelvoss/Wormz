<template>
  <div v-if="book.volumeInfo" class="book-view d-flex flex-column flex-grow-1 margin-left-page margin-right-page">
        <v-row class="d-flex flex-container align-center">
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
                <div class="mt-5">
                    <button class="btnWormz" type="button" @click="open = true">
                        ADICIONAR A
                    </button>
                </div>
            </v-col>
            <v-col cols="6" class="d-flex">
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
        <v-divider class="divider my-10" />
        <v-row class="box-description">
            <p>
                <span class="h3">Descrição</span>
            </p>
            <div class="subtitulo reading-text">{{ book.volumeInfo.description }}</div>
        </v-row>

        <BookShelfDialog @closeDialog="open = false" :dialog="open" />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import BookShelfDialog from '~/components/bib/BookShelfDialog'
export default {
    layout: 'bib',
    components: { BookShelfDialog },
    data(){
        return{
            open: false
        }
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
    font-size: 0.9rem;
    opacity: 80%;
}

.book{
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    background-color: variables.$primary-color;
    border-radius: 15px;
    height: 10vw;
    width: 9vw
}

.divider{
    border-color: $primary-color !important;
}

.flex-container{
    min-height: 18vw;
}

.reading-text{
    font-size: 0.9rem;
}

.btnWormz{
  background: $primary-color;
  border-radius: 20px;
  padding: 0.6vh 1.4vh;
  color: black;
  font-size: 1.5vh;
  font-family: "Encode Sans", sans-serif;

  &:hover{
    background: transparent;
    border: 1px solid $primary-color;
    color: $primary-color;
    transition: 00.5s;
  }
}

</style>