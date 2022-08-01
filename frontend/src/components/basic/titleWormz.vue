<template>
  <div class="title-wormz">
      <v-row align-content="center">

        <v-col cols="5" class="ms-md-12 d-flex justify-center">
            <div class="d-flex flex-column ">
                <div class="h1">Wormz</div>
                <v-divider id="divider" color="#E8E5AE"></v-divider>
                <div class="subtitulo mt-12 text-center">Quer descubrir sua próxima leitura? </div>
                <slot></slot>
                
            </div>
        </v-col>
      </v-row>
  </div>
</template>

<script>
export default {
}
</script>
