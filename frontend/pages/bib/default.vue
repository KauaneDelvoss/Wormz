<template>
  <div class="default d-flex">
    <div class="hide-mobile-l align-center flex-grow-1 justify-center d-flex flex-column ">
      <div class="hide-mobile-l img-wormz mb-10">
        <v-img src="/wormz.png" max-width="10vw"></v-img>
      </div>
      <span class="hide-mobile-l h3">Bem-vindo à sua biblioteca!</span>
    </div>

    <MobileView class="hide-desktop" />
  </div>
</template>

<script>
import MobileView from "~/pages/bib/homeMobile";

export default {
  components: { MobileView },
  layout: "bib",
  middleware: 'auth',
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
