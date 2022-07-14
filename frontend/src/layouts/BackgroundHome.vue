<template>
  <v-app>
      <v-img id='img' src="@/assets/image 2.png">
          <router-view></router-view>
      </v-img>
  </v-app>
</template>

<script>
export default {};
</script>

<style scoped>
template{
    overflow:hidden;
}
#img {
    height: 100vh;
  font-size: 4vw;
  background-size: cover;
  background-repeat: no-repeat;
    overflow-y: hidden;

}
</style>