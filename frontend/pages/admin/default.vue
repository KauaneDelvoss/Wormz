<template>
  <div class="default d-flex">
    <div class="hide-mobile-l align-center flex-grow-1 justify-center d-flex flex-column ">
      <div class="hide-mobile-l img-wormz mb-10">
        <v-img src="/wormz.png" max-width="10vw"></v-img>
      </div>
      <span class="hide-mobile-l h3">Clique para adicionar livros, autores e questões!</span>
    </div>
  </div>
</template>

<script>

export default {
  layout: "admin",
};
</script>

<style scoped lang="scss">
@include breakpoints;

.default {
  min-height: 100vh;
  width: 100%;
  background-color: $secondary-color !important;
}
</style>
