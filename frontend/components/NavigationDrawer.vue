<template>
  <div class="navigation-drawer d-flex align-center">
    <div class="list-wrapper d-flex flex-grow-1 flex-row margin-left-page align-center">
      <div v-for="(item, n) in items" :key="n" class="d-flex list-for mr-7" @click="transitionMaker(item.path)">
        <div v-if="item.path == pageActive" class="d-flex flex-grow-1">
          <div class="d-flex page-box">
            <div class="subtitulo list-item-box">
                {{ item.name.toUpperCase() }}
            </div>
          </div>
        </div>
        <div v-else class="subtitulo list-item">
          {{ item.name.toUpperCase() }}
        </div>
      </div>
    </div>
    <div class="icon-wrapper d-flex flex-row align-center margin-right-page">
      <div class="subtitulo list-item perfil">
          PERFIL
      </div>
      <v-icon class="v-icon-item">mdi-chevron-down</v-icon>
    </div>
    <hr class="divider-item" />
  </div>
</template>

<script>
export default {
    data(){
        return{
            pageActive: '',
            transition: '',
            items: [
              { name: 'Home', path: '/HomeWormz' },
              { name: 'Login', path: '/loginWormz' },
              { name: 'Explorar', path: '/SearchBib'},
              { name: 'Biblioteca', path: '/userBib' },
              { name: 'Quizz', path: '/quizz' },
            ]
        }
    },
    mounted() {
      const route = this.$router.currentRoute.fullPath
      this.pageActive = route
    },
    methods:{
      transitionMaker(path){
        
        if (path != this.pageActive){
          this.transition = ''
          this.pageActive = path
        
          setTimeout(() =>
          {
              return this.$router.push({
                path: path
              });
            }, 200
          )
        }
      }
    }
};
</script>

<style lang="scss" scoped>

.list-for{
  height: 100%;
  cursor: pointer;
}

.list-wrapper{
  height: 100%;
}

.navigation-drawer{
  width: 100vw;
  min-height: $header-height;
  max-height: $header-height;
  background-color: #434c6d;
}

.v-icon-item{
  color: $primary-color;
}

.divider-item{
  top: $header-height;
  width: 100vw;
  color: $primary-color;
  position: absolute;
}

.page-box{
  background-color: $primary-color;
  width: 6vw;
  opacity: 50%;
  justify-content: center;
  margin-top: 10px;
  border-radius: 10% 10% 0 0;
  flex: 1;
}

.list-item-box{
  opacity: 100%;
  color: $bg-color;
}

.list-item, .list-item-box{
  align-self: center;
  justify-self: center;
}


</style>