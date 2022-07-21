<template>
  <div class="login-wormz">
    <v-row class="d-fluid flex-row" style="height: 100vh;">
      <v-col cols="5" class="m-5 d-flex flex-column justify-center">
        <div class="box-input d-flex flex-column align-center" style="gap:3vh;">
          <div class="titulo">
            Login
          </div>
          <div class="forms" v-for="(item, i) in this.items" :key="i" style="width: 70%;">
            <v-text-field
            dark
            color="#E8E5AE"
            v-model=item.vmodel
            :label="item.label"
          ></v-text-field>
          </div>
          <div class="lembrar-senha">
            Não lembro minha senha
          </div>
          <btnWormz :nome="'Entrar'" @click="irPara('home')"></btnWormz>

          <v-row class="box-google d-flex align-center my-2" style="width: 70%; gap: 20px;">
            <v-divider color="#e8e5ae"></v-divider>
            <v-img class="img-google" src="@/assets/Group 4.png"></v-img>
            <v-divider color="#e8e5ae"></v-divider>
          </v-row>
          <v-row class="box-google d-flex align-center justify-center my-2" style="width: 70%; gap: 20px;">
            <div class="lembrar-senha">Não tenho cadastro: </div>
            <btnWormz :nome="'Cadastrar'" @click="irPara('cadastro')"></btnWormz>
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
export default {
  name: "HomeWormz",
  components: { titleWormz, btnWormz },
  data(){
    return{
      roll: 0,
      items: [
        {vmodel: "", label: 'E-mail'},
        {vmodel: "", label: 'Senha'},
        ]
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

<style scoped>
@media only screen and (max-width: 400px) {
    .mobile-hide{ display: none !important; }
    }

.login-wormz {
  height: 100vh;
  width: 100vw;
  background-color: #22273c;
  background-image: url("../assets/blobblue.png");
  background-position: right;
  background-repeat: no-repeat;
  background-size: 100vh;
}

.title-wormz {
  transform: scale(0.7);
}

.box-title {
  position: absolute;
  bottom: 0;
  right: 0;
}

.titulo{
  font-family: "Libre Baskerville", serif;
  font-size: 5vh;
  color: #e8e5ae;
}

.lembrar-senha{
  font-size: 1.5vh;
  color: #e8e5ae;
  text-decoration: underline;
}

.img-google{
  height: 8vh;
  max-width: 8vh;
}
</style>