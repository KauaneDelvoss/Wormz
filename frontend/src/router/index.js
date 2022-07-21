import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeWormz from '../views/HomeWormz.vue'
import searchBib from '../views/SearchBib'
import login from '../views/loginWormz.vue'
import cadastro from '../views/cadastroWormz.vue'

Vue.use(VueRouter)

const routes = [
  {path:'/home', name: 'homeLobby', component: HomeWormz},
  {path:'/searchBib', name:'searchBib', component: searchBib },
  {path:'/login', name:'login', component: login},
  {path:'/cadastro', name:'cadastro', component:cadastro}
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router


