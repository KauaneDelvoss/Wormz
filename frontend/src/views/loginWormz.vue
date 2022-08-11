<template>
  <div class="login-wormz">
    <NavigationDrawer :numActive="1" />
    <v-row class="app d-fluid flex-row" style="height: 100vh;">
      <v-col cols="5" class="m-5 d-flex flex-column justify-center">
        <div class="box-input d-flex flex-column align-center" style="gap:3vh;">
          <div class="titulo">
            Login
          </div>
         <v-text-field
            style="width: 70%;"
            dark
            color="#E8E5AE"
            v-model=userEmail
            label="E-mail"
          ></v-text-field>
         <v-text-field
            style="width: 70%;"
            dark
            color="#E8E5AE"
            v-model=userPassword
            label="Senha"
            :type="show ? 'text' : 'password'"
            :append-icon="show ? 'mdi-eye-off' : 'mdi-eye'"
            @click:append="show = !show"
          ></v-text-field>
          <div class="subtitulo-minimo">
            Não lembro minha senha
          </div>
          <btnWormz :nome="'Entrar'" :path="'searchBib'"></btnWormz>

          <v-row class="box-google d-flex align-center my-2" style="width: 70%; gap: 20px;">
            <v-divider color="#e8e5ae"></v-divider>
            <v-img class="img-google" src="@/assets/images/Group 4.png"></v-img>
            <v-divider color="#e8e5ae"></v-divider>
          </v-row>
          <v-row class="box-google d-flex align-center justify-center my-2" style="width: 70%; gap: 20px;">
            <div class="subtitulo-minimo">Não tenho cadastro: </div>
            <btnWormz :nome="'Cadastrar'" :path="'cadastro'"></btnWormz>
          </v-row>

        </div>
      </v-col>
      <v-col cols="6 m-5 mb-6 d-flex flex-column mobile-hide">
        <div class="box-title d-flex flex-column align-end">
          <titleWormz class="title-wormz"></titleWormz>
        </div>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import titleWormz from "../components/basic/titleWormz.vue";
import btnWormz from "../components/basic/btnWormz.vue";
import NavigationDrawer from "../components/NavigationDrawer.vue"
export default {
  name: "HomeWormz",
  components: { titleWormz, btnWormz, NavigationDrawer },
  data(){
    return{
      roll: 0,
      userEmail: '',
      userPassword: '',
      show: false,
      }
  },
  methods: {
    irPara(local){
      this.$router.push({
        path: '/' + local,
      })
    }
  },
};
</script>

<style lang="sass" scoped>
@use '@/assets/sass/variables'
@use '@/assets/sass/mixins'
.login-wormz 
  height: 100vh
  width: 100vw
  background-color: variables.$bg-color
  background-image: url("../assets/images/blobblue.png")
  background-position: right
  background-repeat: no-repeat
  background-size: 100vh
  overflow: hidden

.title-wormz 
  transform: scale(0.7)

.box-title 
  position: absolute
  bottom: 0
  right: 0

.img-google
  height: 8vh
  max-width: 8vh

</style>