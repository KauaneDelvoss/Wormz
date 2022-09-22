<template>
  <div class="default align-center justify-center d-flex flex-column">
    <div class="img-wormz mb-5">
        <v-img src="/wormz.png" max-width="10vw"></v-img>
    </div>
    <span class="h3">Bem-vindo à sua biblioteca!</span>
  </div>
</template>

<script>
export default {
    layout: 'bib'

}
</script>

<style scoped lang="scss">

.default{
    height: 100vh;
    width: 100%;
    background-color: $secondary-color !important;
}

</style>