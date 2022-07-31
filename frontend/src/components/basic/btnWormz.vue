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

<style scoped>
.btnWormz{
  background: #E8E5AE;
  border-radius: 20px;
  padding: 0.5vw 1.2vw;
}
</style>