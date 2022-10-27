import Vue from "vue";
import Router from "vue-router";

import HomeWormz from "~/pages/HomeWormz";
import loginWormz from "~/pages/loginWormz";
import PerfilUser from "~/pages/PerfilUser";
import SearchBib from "~/pages/SearchBib";
import cadastroUser from "~/pages/cadastro/cadastroWormz";
import UserBib from "~/pages/bib/default";
import bookshelfView from "~/pages/bib/_bookshelf";
import bookView from "~/pages/bib/_book";
import quizzDefault from "~/pages/quizz/default";
import quizzQuestion from "~/pages/quizz/_question";

// Admin
import addBook from "~/pages/admin/addBook";
import adminDefault from "~/pages/admin/default";

Vue.use(Router);

export function createRouter() {
  return new Router({
    mode: "history",
    routes: [
      {
        path: "/",
        component: HomeWormz,
      },
      {
        path: "/loginWormz",
        component: loginWormz,
      },
      {
        path: "/PerfilUser",
        component: PerfilUser,
      },
      {
        path: "/SearchBib",
        component: SearchBib,
      },
      {
        path: "/cadastroUser",
        component: cadastroUser,
      },
      {
        path: "/userBib",
        component: UserBib,
      },
      {
        path: "/userBib/:user?/bookshelf/:id?",
        component: bookshelfView,
      },
      {
        path: "/book/:id?",
        component: bookView,
      },
      {
        path: "/quizz",
        component: quizzDefault,
      },
      {
        path: "/quizz/:id?",
        component: quizzQuestion,
      },

      {
        path: "/admin",
        component: adminDefault,
      },
      {
        path: "/admin/addBook",
        component: addBook,
      },
    ],
  });
}
