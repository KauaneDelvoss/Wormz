<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="55vw">
      <template v-slot:activator="{ on, attrs }">
        <div
          class="
            mb-3
            d-flex
            dropdown-item
            flex-row
            align-center
            header-title
            justify-between
          "
          v-on="on"
          v-bind="attrs"
        >
          CONFIGURAÇÕES
          <v-icon small class="v-icon-item ms-2">mdi-nut</v-icon>
        </div>
      </template>
      <v-card class="card-container">
        <v-card-title>
          <span class="h3 mt-5">Configurações</span>
        </v-card-title>
        <v-card-text>
          <v-container class="container-config py-5 px-5">
            <v-row class="d-flex justify-center">
              <v-col cols="4">
                <div
                  v-for="item in configs"
                  :key="item"
                  class="actions-config subtitulo my-10"
                  @click="activeConfig = item"
                >
                  {{ item }}
                </div>
              </v-col>
              <v-col cols="5">
                  <div v-if="activeConfig = configs[0]">
                    <user />
                  </div>
                  <!-- continua -->
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialog = false, saveConfig()">
            Close
          </v-btn>
          <v-btn color="blue darken-1" text @click="dialog = false, clearInput()">
            Save
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
  data() {
    return {
      dialog: false,
      configs: ["Perfil", "Estantes", "Google Books"],
      activeConfig: "Perfil",
    };
  },
};
</script>

<style lang="scss" scoped>
.template{
    overflow-y: hidden;
}
.dropdown-item:hover {
  text-decoration: underline;
  cursor: pointer;
}

.dropdown-item {
  color: $primary-color;
}

.card-container {
  background-color: $secondary-color;
}

.container-config {
  border: 1px solid $primary-color;
}

.actions-config {
  cursor: pointer;
}

</style>