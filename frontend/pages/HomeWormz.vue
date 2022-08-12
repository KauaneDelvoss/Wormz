<template>
  <v-app>
    <ImgBackground>
      <router-view></router-view>
      <titleWormz style="height: 100vh;" class="app d-flex align-center">
        <btnWormz :path="'loginWormz'" :nome="'Entrar'" class="mt-10 align-self-center"></btnWormz>
      </titleWormz>
    </ImgBackground>
  </v-app>
</template>

<script>
export default {
  name: "HomeWormz",
  methods: {
    irPara(local){
      this.$router.push({
        path: "/" + local
      })
    }
  }
}
</script>



<style scoped>
template{
    overflow:hidden;
    
}

.img-hover{
  cursor: pointer;
}

</style>