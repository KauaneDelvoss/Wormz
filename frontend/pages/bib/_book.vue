<template>
  <div
    v-if="book"
    class="book-view d-flex mb-4 flex-column flex-grow-1 margin-left-page margin-right-page mt-10"
  >
    <v-row class="d-flex flex-container align-center">
      <v-col cols="6">
        <v-row class="align-center mb-3">
          <span class="h3">{{ book.name_book }}</span>
          <v-icon class="ms-5 v-icon-item" @click="book.liked = false" v-if="book.liked">mdi-cards-heart</v-icon>
          <v-icon class="ms-5 v-icon-item" @click="book.liked = true" v-else>mdi-cards-heart-outline</v-icon>
        </v-row>
        <div>
          <div v-for="author in book.author" :key="author">
            <span class="subtitulo"> {{ author }} </span>
          </div>
          <!-- <span class="subtitulo data">
            {{ book.volumeInfo.publishedDate }}
          </span> -->
        </div>
        <v-row class="align-center mt-2">
          <v-rating
            class="rating"
            empty-icon="mdi-star-outline"
            full-icon="mdi-star"
            half-icon="mdi-star-half-full"
            half-increments
            length="5"
            readonly
            size="20"
            :value="reviewCount"
          ></v-rating>
          <span class="subtitulo data">{{ reviews.length }} reviews</span>
        </v-row>
        <div class="mt-5">
          <button class="btnWormz" type="button" @click="open = true">
            ADICIONAR A
          </button>
        </div>
      </v-col>
      <v-col cols="6" class="d-flex">
        <v-card class="mx-auto book">
          <v-img
            v-if="book.capa"

            :src="book.capa.url"
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
      <div class="subtitulo reading-text">
        {{ book.resume }}
      </div>
    </v-row>
    <v-divider class="divider my-10" />

    <div class="reviews-container">
            <p>
                <span class="h3">Comentários</span>
            </p>
        <div class="user-review d-flex">
            <ReviewAction @submitReview="getReviews()" :book="book" />
        </div>
        <div class="show-reviews mt-10 mb-10">
            <ReviewView :reviews="reviews" />
        </div>
    </div>

    <BookShelfDialog @closeDialog="open = false" :dialog="open" :book="book.id" />
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import BookShelfDialog from "~/components/bib/BookShelfDialog";
import ReviewAction from "~/components/bib/ReviewAction";
import ReviewView from "~/components/bib/ReviewView";

export default {
  layout: "bib",
  middleware: 'auth',
  components: { BookShelfDialog, ReviewAction, ReviewView },
  data() {
    return {
      open: false,
      reviews: {},
      reviewCount: 0
    };
  },
  mounted() {
    const id = this.$router.currentRoute.params.id;
    // this.$store.dispatch("book/GET_URL", id);
    this.GET_BOOK(id)
    this.getReviews()

  },
  computed: {
    ...mapState("book", ["book"]),
  },
  methods:{
    ...mapActions("book", ["GET_BOOK"]),
    getReviews(){
      this.$axios.$get('get/reviews/' + this.book.id).then(
        response => {
          console.log(response)
          this.reviews = response
        }
      )
    },
    reviewCount(){
      // vc esta aqui
    }
  }
};
</script>

<style scoped lang="scss">

.data {
  font-size: 0.9rem;
  opacity: 80%;
}

.book {
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  background-color: variables.$primary-color;
  border-radius: 15px;
  height: 10vw;
  width: 9vw;
}

.flex-container {
  min-height: 18vw;
}

.btnWormz {
  background: $primary-color;
  border-radius: 20px;
  padding: 0.6vh 1.4vh;
  color: black;
  font-size: 1.5vh;
  font-family: "Encode Sans", sans-serif;

  &:hover {
    background: transparent;
    border: 1px solid $primary-color;
    color: $primary-color;
    transition: 00.5s;
  }
}

</style>
