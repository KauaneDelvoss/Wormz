<template>
  <div class="box-input d-flex flex-column align-center" style="gap:3vh;">
          <v-autocomplete
            style="width: 70%;"
            dark
            color="#E8E5AE"
            v-model="userPais"
            label="País (opcional)"
            :items="paises"
          ></v-autocomplete>
         <v-autocomplete
            style="width: 70%;"
            dark
            color="#E8E5AE"
            v-model="userEstado"
            label="Estado (opcional)"
            type="text"
            :items="estados"
          ></v-autocomplete>
         <v-autocomplete
            style="width: 70%;"
            dark
            color="#E8E5AE"
            v-model="userCidade"
            label="Cidade (opcional)"
            type="text"
            :items="cidades"
          ></v-autocomplete>
          <slot></slot>
        </div>
</template>

<script>
export default {
    data(){
        return{
            userPais: '',
            userEstado: '',
            userCidade: '',
            paises: ['Brasil', 'Argentina', 'Paraguai'],
            estados: ['Santa Catarina', 'Sergipe', 'Maranhão', 'Paraná'],
            cidades: ['Florianópolis', 'Curitiba', 'Balneário Camboriú']
        }
    }
}
</script>

<style>

</style>