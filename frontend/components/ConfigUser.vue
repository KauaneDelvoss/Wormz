<template>
  <v-row justify="center" class="dialog">
    <v-dialog transition="dialog-bottom-transition" v-model="dialog" class="dialog" persistent :max-width="width">
      <v-card class="card-container">
        <v-card-title>
          <span class="h3 mt-5">Configurações</span>
        </v-card-title>
        <v-card-text>
          <v-container class="container-config py-5 px-5">
            <v-row class="d-flex justify-center">
              <v-row class="row-div flex-column mx-2">
                <div v-for="(item, index) in configs" :key="index" class="actions-config subtitulo my-10"
                  @click="activeConfig = index">

                  <div v-if="activeConfig == index" style="text-decoration: underline;">
                    {{ item }}
                  </div>
                  <div v-else> {{ item }} </div>

                </div>
              </v-row>
              <v-row>
                <div v-if="activeConfig == 0">
                  <user @fechar="$emit('close')" />
                </div>
                <!-- continua -->
              </v-row>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn class="dropdown-item" text @click="$emit('close')">
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import user from "~/components/configUser/user";
export default {
  components: { user },
  props: { dialog: Boolean },
  data() {
    return {
      configs: ["Perfil", "Estantes", "Google Books"],
      activeConfig: 0,

    };
  },
  computed: {
    width() {
      switch (this.$vuetify.breakpoint.name) {
        case 'xs': return 900
        case 'sm': return 800
        case 'md': return 600
        case 'lg': return 700
        case 'xl': return 1000
      }
    }
  }
};
</script>

<style lang="scss" scoped>
@include breakpoints;

@media (max-width: $phone_l) {
  .dialog {
    max-width: 100vw !important;
    width: 100vw !important;
  }

  .row-div {
    justify-items: space-around
  }

  .row-div {
    flex-direction: row !important;
  }
}

.dropdown-item:hover {
  text-decoration: underline;
  cursor: pointer;
}

.dropdown-item {
  color: $primary-color;
}

.card-container {
  background-color: $bg-color;
}

.container-config {
  border: 1px solid $primary-color;
}

.actions-config {
  cursor: pointer;
}

.actions-config:hover {
  text-decoration: underline;
}
</style>
