<template>
  <ImgBackground>
    <div class="question-quizz d-flex align-center justify-center">
      <div class="d-flex flex-column">
        <v-row class="justify-space-between mb-5">
          <v-icon large class="v-icon-item">mdi-arrow-left</v-icon>
          <div class="h3">Questão {{ question_id }} de 5</div>
          <v-icon v-if="question_id != 6" large class="v-icon-item"
            >mdi-arrow-right</v-icon
          >
          <v-icon v-else large class="v-icon-item">mdi-check-bold</v-icon>
        </v-row>
        <div
          class="
            card
            d-flex
            align-center
            justify-space-between
            flex-column
            py-10
          "
        >
          <div id="oi" class="d-flex flex-column" >
            <div
              class="subtitulo little justify-self-end"
              v-for="pergunta in perguntas"
              :key="pergunta.id"
              v-show="pergunta.id == question_id"
            >
              <h1>{{ pergunta.book }} - {{ pergunta.author }}</h1>
              <h3>
                {{ pergunta.snip }}
              </h3>
            </div>
          </div>
          <div
            v-for="resposta in respostas"
            :key="resposta.id"
            class="justify-content"
          >
            <div id="radio" class="radio-box d-flex flex-row">
              <v-icon
                small
                class="v-icon-item"
                v-if="answer_id == resposta.id"
                @click="answer_id = resposta.id"
                >mdi-circle-slice-8</v-icon
              >
              <v-icon
                small
                class="v-icon-item"
                v-else
                @click="answer_id = resposta.id"
                >mdi-circle-outline</v-icon
              >
              <div class="subtitulo mb-2">{{ resposta.subtitle }}</div>
            </div>
          </div>
          <div>
            <button
              type="button"
              class="btnWormz"
              v-show="(question_id < 5)"
              @click="proximo()"
            >
              proximo
            </button>
            <button
              type="button"
              v-show="(question_id == 5)"
              class="btnWormz"
              @click="(proximo(), $router.push('/userBib'),bookshelfQuiz())"
            >
              enviar
            </button>
          </div>
        </div>
      </div>
    </div>
  </ImgBackground>
</template>

<script>
import ImgBackground from "~/components/basic/ImgBackground";
import { mapState } from "vuex";

export default {
  components: { ImgBackground },
  middleware: 'auth',
  data() {
    return {
      contador : 0,
      question_id: 1,
      answer_id: 0,
      url : '',
      answer: {
        user: 0,
        cod_answer: 0,
        cod_question: 1,
        cod_forms: 1, //sem dinamicidade com o id do quizz ainda,
        genre: ""
      },
      genres: [
        { name: "fantasia", contador: 0 },
        { name: "ficcao", contador: 0 },
        { name: "filosofia", contador: 0 },
      ],

      respostas: [
        { id: 1, subtitle: "Gostei" },
        { id: 2, subtitle: "Não tenho certeza" },
        { id: 3, subtitle: "Não gostei" },
      ],

      perguntas: [
        {
          id: 1,
          snip: "O que você acha da seguinte história: Ela roubou uma vida. Agora deve pagar com o coração. Acompanhe as aventuras de Feyre pelo perigoso e deslumbrante mundo das fadas. ",
          book: "Corte de Espinhos e Rosas",
          author: "Sarah J. Maas",
          genres: "fantasia",
        },
        {
          id: 2,
          snip: "Seu tema central - um personagem que leva uma vida dupla, mantendo uma aparência de virtude enquanto se entrega ao hedonismo mais extremado, com a presença de elementos fantásticos e de grandes reflexões filosóficas, além do senso de humor sagaz e do sarcasmo implacável",
          book: "O Retrato de Dorian Gray",
          author: "Oscar Wilde",
          genres: "filosofia",
        },
        {
          id: 3,
          snip: "O que você acha da seguinte história: “De capítulo em capítulo, de “lição” em “lição”, o leitor é convidado a percorrer toda a história da filosofia ocidental, ao mesmo tempo que se vê envolvido por um thriller que toma um rumo surpreendente.",
          book: "O mundo de Sofia",
          author: "Jostein Gaarder",
          genres: "filosofia",
        },
        {
          id: 4,
          snip: "O que você acha da seguinte história: “Narra a insurreição dos animais de uma granja contra seus donos. Progressivamente, porém, a revolução degenera numa tirania ainda mais opressiva que a dos humanos.",
          book: "Outra coisa ne",
          author: "Jorge Orwell",
          genres: "filosofia",
        },
        {
          id: 5,
          snip: "O que você acha da seguinte história: A magia há muito abandonou Adarlan.  Um perverso rei governa, punindo impiedosamente as minorias rebeldes. Mas tudo pode mudar quando uma assassina é chamada para o castelo.",
          book: "Trono de Vidro",
          author: "Sarah J. Maas",
          genres: "fantasia",
        },
      ],
    };
  },
  computed: {
    ...mapState("auth", ["user"]),
  },
  methods: {
    proximo() {
      if (
        this.answer_id === this.respostas[0].id
      ) {
        var g = this.perguntas[this.question_id - 1].genres; //descobrindo o gênero da pergunta
        var result = this.genres.find((genre) => {
          if (genre.name === g) {
            genre.contador += 1;
            return result;
          } //filtrando os gêneros por nome e adicionando um contador no gênero igual à const g (o gênero da pergunta).
          else {
          }
        });
      } else if (
        this.answer_id === this.respostas[2].id
      ) {
        var g = this.perguntas[this.question_id - 1].genres; //descobrindo o gênero da pergunta
        var result = this.genres.find((genre) => {
          if (genre.name === g) {
            genre.contador -= 1;
            return result;
          } //filtrando os gêneros por nome e adicionando um contador no gênero igual à const g (o gênero da pergunta).
          else {
          }
        });
      }
      console.log("Fantasia: " +this.genres[0].contador);
      console.log("Ficção: " + this.genres[1].contador);
      console.log("Filosofia: " + this.genres[2].contador);
      this.enviar()
    },
    async enviar() {
      this.answer.cod_answer = this.answer_id;
      this.answer.cod_question = this.question_id;
      this.answer.user = this.user.id;
      try {
        const quizResponse = (
          await this.$axios.post("/quizz/create", JSON.stringify(this.answer), {
            headers: { "Content-Type": "application/json" },
          })
        ).data;
        console.log(quizResponse);
      } catch (e) {
        return Promise.reject(e);
      }
      console.log("O resultado desses contadores fica no componente Vue. O que sobe para o banco é o id_pergunta + id_resposta + cod_form")
      this.question_id += 1; //adicionando contador para mudar de pergunta
    },
    bookshelfQuiz() {

      this.answer.cod_answer = this.answer_id;
      this.answer.cod_question = this.question_id;
      this.answer.user = this.user.id;
      this.answer.genre = "fantasia"

      const a = (this.$axios.post("/quizz/bookshelf", JSON.stringify(this.answer), {
              headers: { "Content-Type": "application/json" },
            })).data;
          console.log(a)
    },  
    
  },

  mounted() {
    this.id = this.$router.currentRoute.params.id;
  },

};
</script>

<style scoped lang="scss">
@media (max-width: $phone_l) {
  .card {
    width: 90vw !important;
  }
}
  #oi {
  padding: 0vh 2vw 0vh 2vw
}
.v-application .py-10 {
    padding-top: 30px !important;
    padding-bottom: 20px !important;
    padding-left: 1vh;
    padding-right: 1vh;
}
  #radio {
    padding: 0px;
    margin: 0px 0px 0px 0px;
  }
.question-quizz {
  height: 100vh;
}

.card {
  height: 50vh;
  width: 50vw;
  background-color: $bg-color !important;
  border-radius: 20px;
  border: 1px solid $primary-color;
}
</style>
