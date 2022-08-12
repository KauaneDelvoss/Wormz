<template>
  <v-img id="img" src="/background.png">
  <slot></slot>
  </v-img>
</template>

<script>
export default {

}
</script>

<style lang="scss" scoped>

#img {
  height: $template-height;
  background-size: cover;
  background-repeat: no-repeat;
  overflow: hidden;

}

</style>