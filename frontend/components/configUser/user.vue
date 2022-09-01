<template>
  <div>
    <div class="subtitulo">Alterar informações:</div>
    <div class="row-wrapper">
      <div class="box-config-user d-flex flex-row align-center">
        <div class="header-title me-3">Foto:</div>
        <v-file-input
          label="Foto"
          prepend-icon="mdi-camera"
          dark
        ></v-file-input>
      </div>
    </div>
    <div class="row-wrapper">
      <div class="box-config-user d-flex flex-row align-center">
        <div class="header-title me-3">Nome:</div>
        <v-text-field value="nickname do user" dark></v-text-field>
      </div>
      <div class="box-config-user d-flex flex-row align-center">
        <div class="header-title me-3">E-mail:</div>
        <v-text-field value="e-mail do user" dark></v-text-field>
      </div>
      <div class="box-config-user d-flex flex-row align-center">
        <div class="header-title me-3">Senha:</div>
        <v-text-field value="password do user" dark></v-text-field>
      </div>
    </div>

    <div class="row-wrapper">
      <div class="box-config-user d-flex flex-row align-center">
        <div class="header-title me-3">País:</div>
        <v-text-field value="país do user" dark></v-text-field>
      </div>
      <div class="box-config-user d-flex flex-row align-center">
        <div class="header-title me-3">Estado:</div>
        <v-text-field value="país do user" dark></v-text-field>
      </div>
      <div class="box-config-user d-flex flex-row align-center">
        <div class="header-title me-3">Cidade:</div>
        <v-text-field value="país do user" dark></v-text-field>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.row-wrapper {
  background: rgba(232, 229, 174, 0.2);
  padding: 20px;
  margin: 20px;
  border-radius: 20px;
}

</style>