<template>
  <button class="btnWormz" type="button" @click="irPara(path)">{{nome}}</button>
</template>

<script>
export default {
    props:{nome:String, path:String},
    methods:{
      irPara(path){
        if(path){
          this.$router.push({
            path: '/' + path
          })
        } else {
          this.$emit('sliderCount')
        }
      }
    }
}
</script>

<style lang="sass" scoped>
@use '@/assets/sass/_variables.sass'

.btnWormz
  background: variables.$primary-color
  border-radius: 20px
  padding: 0.5vw 1.2vw

  &:hover
    background: transparent
    border: 1px solid variables.$primary-color
    color: variables.$primary-color
    transition: 00.5s
</style>