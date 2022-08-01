<template>
  <v-img id="img" src="@/assets/images/image 2.png">
  <slot></slot>
  </v-img>
</template>

<script>
export default {

}
</script>

<style scoped>

#img {
  height: 100vh;
  background-size: cover;
  background-repeat: no-repeat;
  overflow-y: hidden;

}

</style>