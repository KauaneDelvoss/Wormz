<template>
  <button class="btnWormz" type="button">{{nome}}</button>
</template>

<script>
export default {
    props:{nome:String}
}
</script>

<style scoped>
.btnWormz{
  background: #E8E5AE;
  border-radius: 20px;
  padding: 0.5vw 1.2vw;
}
</style>