<template>
  <v-app>
    <ImgBackground>
    <NavigationDrawer :numActive="0" />
      <router-view></router-view>
      <titleWormz style="height: 100vh;" class="app d-flex align-center">
        <btnWormz :path="'login'" :nome="'Entrar'" class="mt-10 align-self-center"></btnWormz>
      </titleWormz>
    </ImgBackground>
  </v-app>
</template>

<script>
import ImgBackground from "../components/basic/ImgBackground.vue"
import titleWormz from "../components/basic/titleWormz.vue"
import btnWormz from "../components/basic/btnWormz.vue"
import NavigationDrawer from "../components/NavigationDrawer.vue"
export default {
  name: "HomeWormz",
  components: { ImgBackground, titleWormz, btnWormz, NavigationDrawer },
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