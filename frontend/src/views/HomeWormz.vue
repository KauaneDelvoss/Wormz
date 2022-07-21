<template>
  <v-app>
    <ImgBackground>
      <router-view></router-view>
      <titleWormz style="height: 100vh;" class="d-flex align-center">
        <v-img width='8vh' @click="irPara('login')" src="../assets/Group 4.png" class="mt-10 align-self-center img-hover"></v-img>
      </titleWormz>
    </ImgBackground>
  </v-app>
</template>

<script>
import ImgBackground from "../components/basic/ImgBackground.vue"
import titleWormz from "../components/basic/titleWormz.vue"
export default {
  name: "HomeWormz",
  components: { ImgBackground, titleWormz },
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