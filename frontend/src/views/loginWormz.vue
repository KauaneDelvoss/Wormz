<template>
  <div class="login-wormz">
    <v-row class="d-fluid flex-row" style="height: 100vh;">
      <v-col cols="5" class="m-5 d-flex flex-column justify-center">
        <div class="box-input d-flex flex-column align-center" style="gap:3vh;">
          <div class="titulo">
            Cadastro
          </div>
          <v-text-field
            color="#E8E5AE"
            style="width: 70%"
            v-model="inputEmail"
            label="E-mail"
          ></v-text-field>
          <v-text-field 
            color="#E8E5AE"
            style="width: 70%"
            v-model="inputSenha"
            label="Senha"
          ></v-text-field>
          <v-text-field 

            style="width: 70%"
            v-model="inputConfirmarSenha"
            label="Confirme a Senha"
          ></v-text-field>
          <btnWormz :nome="'Prosseguir'"></btnWormz>
        </div>
      </v-col>
      <v-col cols="6 m-5 mb-6 d-flex flex-column">
        <div class="box-title d-flex flex-column align-end">
          <titleWormz class="title-wormz"></titleWormz>
        </div>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import titleWormz from "../components/titleWormz.vue";
import btnWormz from "../components/basic/btnWormz.vue";
export default {
  name: "HomeWormz",
  components: { titleWormz, btnWormz },
  methods: {},
};
</script>

<style scoped>
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
</style>