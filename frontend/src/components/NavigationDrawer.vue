<template>
  <div class="navigation-drawer">
    <div class="list-wrapper">
      <div v-for="(item, n) in items" :key="n">
        <div class="list-item">
            {{ item }}
        </div>
      </div>
       <div class="list-item perfil">
            Perfil
        </div>
    </div>
  </div>
</template>

<script>
export default {
    data(){
        return{
            items: ['Home', 'Login'],
        }
    }
};
</script>

<style>
@media only screen and (max-width: 500px) {
  .navigation-drawer {
    display: none !important;
  }
}

.navigation-drawer {
  width: 100vw;
  height: 7vh;
  background-color: #434c6d;
}
</style>