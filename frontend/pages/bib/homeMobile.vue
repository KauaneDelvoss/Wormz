<template>
  <div class="bib-view-mobile">
    <v-row class="mobile-profile mt-12">
      <v-col class="ms-md-12 d-flex flex-column align-center col-default">
        <div class="d-flex flex-column">
          <div class="h1">Wormz</div>
          <v-divider id="divider" class="mb-n4" color="#E8E5AE"></v-divider>
          <div class="subtitulo mt-10 text-center">
            Procure na sua biblioteca:
          </div>
        </div>
      </v-col>
    </v-row>

    <div class="form-container d-flex flex-column align-center mt-4">
      <input
        type="text"
        name="form-container"
        placeholder="Blade Runner..."
        id="form-area"
        v-model="searchField"
        @keyup="search(searchField)"
        class="subtitulo ps-2"
      />
      <v-icon
        small
        style="width: 100%; left: 15vw"
        class="flex-column align-start my-2"
        color="#e8e5ae"
        >mdi-filter-menu</v-icon
      >
    </div>

    <div class="margin-left-page margin-right-page my-5">
      <div
        class="
          margin-left-page margin-right-page
          static-data
          d-flex
          flex-row
          my-5
          align-center
        "
      >
        <v-avatar color="grey lighten-2" size="60" tile></v-avatar>
        <div class="text-box">
          <div class="subtitulo font-weight-bold ms-3">Indicações</div>
          <div class="subtitulo ms-3">Atualizado em: 12/10/2022</div>
        </div>
      </div>
      <div
        class="
          margin-left-page margin-right-page
          static-data
          d-flex
          flex-row
          my-5
          align-center
        "
      >
        <v-avatar color="grey lighten-2" size="60" tile></v-avatar>
        <div class="text-box">
          <div class="subtitulo font-weight-bold ms-3">Curtidos</div>
          <div class="subtitulo ms-3">123 livros</div>
        </div>
      </div>

      <v-divider class="divider" />

      <div
        v-for="bookshelf in bookshelves"
        :key="bookshelf.id"
        class="
          margin-left-page margin-right-page
          static-data
          d-flex
          flex-row
          my-5
          align-center
        "
        @click="goTo(bookshelf.id)"
      >
        <v-avatar color="grey lighten-2" size="60" tile></v-avatar>
        <div class="text-box">
          <div class="subtitulo font-weight-bold ms-3">
            {{ bookshelf.name }}
          </div>
          <div class="subtitulo ms-3">{{ bookshelf.num_books }} livros</div>
        </div>
      </div>
    </div>
    <FloatingButton />
  </div>
</template>

<script>
import FloatingButton from '~/components/basic/FloatingButton'

export default {
  components: { FloatingButton },
  data() {
    return {
      searchField: "",
      bookshelves: [
        { id: 1, name: "enteropígrafe", num_books: 42 },
        { id: 2, name: "match com kakau", num_books: 10 }
    ],
    };
  },
  methods: {
    goTo(id) {
      this.$router.push({
        path: "/userBib/bookshelf/" + id,
      });
    },
  },
};
</script>

<style scoped lang="scss">
@include breakpoints;

.bib-view-mobile {
  background-image: linear-gradient(
    45deg,
    $bg-color,
    $secondary-color
  ) !important;
  min-height: 100vh;
  width: 100vw;
  overflow: hidden;
}

#form-area {
  width: 70vw;
  height: 4vh;
  background-color: rgb(232, 229, 174, 0.64);
  border-radius: 20px;
  padding-left: 2vw;
}

.icon-search {
  position: relative;
  width: 1%;
}

.card {
  border-radius: 15px;
  background-color: $primary-color;
}
</style>