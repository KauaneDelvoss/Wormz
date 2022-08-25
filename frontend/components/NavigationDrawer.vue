<template>
  <div class="navigation-drawer d-flex align-center">
    <div class="margin-left-page hide-desktop">
      <v-icon class="v-icon-item" @click="$emit('activeToggle', !toggleBar)">mdi-view-headline</v-icon>
    </div>
    <div class="list-wrapper d-flex flex-grow-1 flex-row margin-left-page align-center hide-mobile-l">
      <div v-for="(item, n) in items" :key="n" class="d-flex list-for mr-7" @click="transitionMaker(item.path)">
        <div v-if="item.path == pageActive" class="d-flex flex-grow-1">
          <div class="d-flex page-box">
            <div class="header-title list-item-box">
                {{ item.name.toUpperCase() }}
            </div>
          </div>
        </div>
        <div v-else class="header-title list-item">
          {{ item.name.toUpperCase() }}
        </div>
      </div>
    </div>
    <div class="icon-wrapper d-flex flex-row align-center margin-right-page hide-mobile-l">
      <div class="header-title list-item perfil" @click="showProfile()">
          PERFIL
      </div>
      <v-icon class="v-icon-item" @click="show = !show">mdi-chevron-down</v-icon>
    </div>

    <div class="box-show" v-if="show">OI</div> <!-- vc esta aqui -->
    <hr class="divider-item" />
  </div>
</template>

<script>
export default {
  props: {activeToggleBar: Boolean}  ,
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
            ],
            toggleBar: false,
            show: false,
        }
    },
    mounted() {
      let route = this.$router.currentRoute.path
      this.pageActive = route

      this.toggleBar = this.activeToggleBar
    },

    methods:{
      transitionMaker(path){
        
        if (path != this.pageActive){
          this.pageActive = path
          this.transition = ''
        
          setTimeout(() =>
          {
              return this.$router.push({
                path: path
              });
            }, 200
          )
        }
      },
    },
    watch: {
      '$route' (to, from){
        this.pageActive = to.path
      }
    }
};
</script>

<style lang="scss" scoped>
@include breakpoints;

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