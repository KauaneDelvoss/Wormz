<template>
  <v-card v-if="book.capa" class="mx-auto book" @click="goToBook(book.id)">
    <v-img
      v-if="book.capa"
      :src="book.capa.url"
      height="28vh"
      aspect-ratio="1.7"
    >
      <div class="fill-height bottom-gradient">
        <div class="card-icon ps-3 pt-3">
          <v-icon v-if="book.liked" @click="likeBook(book.id)" class="icon"
            >mdi-cards-heart-outline</v-icon
          >
          <v-icon v-else class="icon" @click="likeBook(book.id)"
            >mdi-cards-heart</v-icon
          >
        </div>

        <v-card-actions>
          <v-btn
            text
            color="variables.$primary-color"
            class="v-card-show"
            @click="reveal = true"
          >
            Olhadinha
          </v-btn>
        </v-card-actions>
      </div>
    </v-img>

    <div v-else class="not-found"></div>

    <v-expand-transition>
      <v-card
        v-if="reveal"
        class="transition-fast-in-fast-out v-card--reveal book"
        style="height: 100%"
      >
        <v-card-text>
          <div v-for="item in book.author" :key="item">
            {{ item }}
          </div>
          <div class="header-title text--primary">
            {{ book.book_name }}
          </div>
          <!-- <p>{{ book.volumeInfo.publishedDate }}</p> -->
        </v-card-text>
        <v-card-actions class="pt-0">
          <v-btn text class="v-card-show" @click="reveal = false">
            Fechar
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-expand-transition>
  </v-card>
</template>

<script>
export default {
  props: ['book'],
  data: () => ({
    reveal: false,
  }),
  methods: {
    likeBook(id) {
      this.$store.commit("search_books/LIKE_BOOK", id);
    },
    goToBook(id) {
      this.$router.push({
        path: '/book/' + id
      })
    }
  },
};
</script>

<style lang="sass" scoped>
@use '~/assets/sass/variables'

@media (max-width: variables.$phone_l)
  .book
    width: 35vw !important

@media (max-width: variables.$tablet_xl)
  .book
    width: 18vh !important


.bottom-gradient
  background-image: linear-gradient(90deg, rgba(0,0,0,0.3) 0%, rgba(0,0,0,0.3) 100%)

.book
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25)
  background-color: variables.$primary-color
  border-radius: 15px
  width: 9vw
  height: 28vh

.card-icon
  margin-right: 0
  width: 100%
  position: relative
  justify-items: flex-end

.icon
  color: variables.$primary-color

.v-card-show
  position: absolute
  bottom: 0
  left: 0
  color: variables.$primary-color
  background-image: linear-gradient(90deg, rgba(0,0,0,0.3) 0%, rgba(0,0,0,0.3) 100%)
  border-radius: 0 20px 20px 0
  text-decoration: underline

.v-card--reveal
  bottom: 0
  opacity: 1 !important
  position: absolute
  width: 100%

  .not-found
    background-color: variables.$primary-color
</style>
