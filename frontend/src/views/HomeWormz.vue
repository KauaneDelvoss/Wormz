<template>
  <v-app>
    <ImgBackground>
      <router-view></router-view>
      <titleWormz>
        <v-img width='8vh' @click="irPara('login')" src="../assets/Group 4.png" class="mt-10 align-self-center img-hover"></v-img>
      </titleWormz>
    </ImgBackground>
  </v-app>
</template>

<script>
import ImgBackground from "../components/ImgBackground.vue"
import titleWormz from "../components/titleWormz.vue"
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