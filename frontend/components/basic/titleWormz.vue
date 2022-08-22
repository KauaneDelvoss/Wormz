<template>
  <div class="title-wormz">
      <v-row align-content="center">

        <v-col class="ms-md-12 d-flex flex-column align-center col-default">
            <div class="d-flex flex-column">
                <div class="h1">Wormz</div>
                <v-divider id="divider" color="#E8E5AE"></v-divider>
                <div class="subtitulo mt-12 text-center">Quer descubrir sua próxima leitura? </div>
                <slot></slot>
                
            </div>
        </v-col>
      </v-row>
  </div>
</template>

<style lang="sass" scoped>
@use '~/assets/sass/style'
@use '~/assets/sass/mixins'
@include mixins.breakpoints
</style>
