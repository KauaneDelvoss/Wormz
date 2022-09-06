import Vue from 'vue'
import Router from 'vue-router'

import HomeWormz from '~/pages/HomeWormz'
import loginWormz from '~/pages/loginWormz'
import PerfilUser from '~/pages/PerfilUser'
import SearchBib from '~/pages/SearchBib'
import cadastroUser from '~/pages/cadastro/cadastroWormz'

Vue.use(Router)

export function createRouter() {
  return new Router({
    mode: 'history',
    routes: [
      {
        path: '/',
        component: HomeWormz
      },
      {
        path: '/loginWormz',
        component: loginWormz
      },
      {
        path: '/PerfilUser',
        component: PerfilUser
      },
      {
        path: '/SearchBib',
        component: SearchBib
      },
      {
        path: '/cadastroUser',
        component: cadastroUser
      },
    ]
  })
}
