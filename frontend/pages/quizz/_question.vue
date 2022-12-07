<template>
  <ImgBackground>
    <div class="question-quizz d-flex align-center justify-center">
      <div class="d-flex flex-column">
        <v-row class="justify-space-between mb-5">
          <v-icon large class="v-icon-item">mdi-arrow-left</v-icon>
          <div class="h3">Questão {{ question_id }} de 10</div>
          <v-icon v-if="question_id != 10" large class="v-icon-item">mdi-arrow-right</v-icon>
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
          <div class="d-flex flex-column ">
            <div class="subtitulo little justify-self-end" v-for="pergunta in perguntas"  v-show:key="(pergunta.id ==  question_id)" >
              <h1>
                {{ pergunta.book }} - {{ pergunta.author }}
              </h1>
              <h3>
                {{ pergunta.snip }}
              </h3>
            </div>
          </div>
          <div v-for="resposta in respostas" :key="resposta.id" class="justify-content">
          

            <div class="radio-box d-flex  flex-row" >
              <v-icon
              small
              class="v-icon-item"
              v-if="perguntas[question_id-1].selected == resposta.id"
              @click="perguntas[question_id].selected = resposta.id"
              >mdi-circle-slice-8</v-icon
              >
              <v-icon small class="v-icon-item" v-else @click="perguntas[question_id-1].selected = resposta.id"
              >mdi-circle-outline</v-icon
              >
              <div class="subtitulo mb-2"
               >{{resposta.subtitle}}</div>
            </div>

          </div >
          <div>
            <button type="button" class="btnWormz mt-5 green" @click="proximo() ">proximo</button>
            <button type="button" v-show="(question_id == 3)" class="btnWormz mt-5 green" @click="enviar() ">enviar</button>

            informações: {{question_id}} {{perguntas[question_id-1].selected}}
          </div>


        </div>
      </div>
    </div>
  </ImgBackground>
</template>

<script>
import ImgBackground from "~/components/basic/ImgBackground";

export default {
  components: { ImgBackground },
  data() {
    return {

      question_id: 1,
      answer: {
        user: 1,
        cod_answer: 1 ,
        cod_question: 1 ,
      },
      genres: [
        {name: "fantasia", contador: 0},
        {name: "ficcao", contador: 0},
        {name: "filosofia", contador: 0}

      ],

      respostas: [
        { id: 1, subtitle:"Gostei"},
        { id: 2, subtitle: "Não tenho certeza"},
        { id: 3, subtitle: "Não gostei"}
      ],
      
      perguntas:  [ {
        id : 1,
        snip: "O que você acha da seguinte história: Ela roubou uma vida. Agora deve pagar com o coração. Acompanhe as aventuras de Feyre pelo perigoso e deslumbrante mundo das fadas. ",
        selected: "",
        book: "Corte de Espinhos e Rosas",
        author: "Sarah J. Maas",
        genres: "fantasia"

      },
      {
        id : 2,
        snip: "fdgdia: Ela roubou uma vida. Agora deve pagar com o coração. Acompanhe as aventuras de Feyre pelo perigoso e deslumbrante mundo das fadas. ",
        selected: "",
        book: "Outra coisa ne",
        author: "blz",
        genres: "fantasia"

      },
      {
        id : 3,
        snip: "fdgdia: Ela roubou uma vida. Agora deve pagar com o coração. Acompanhe as aventuras de Feyre pelo perigoso e deslumbrante mundo das fadas. ",
        selected: "",
        book: "Outra coisa ne",
        author: "blz",
        genres: "ficcao"

      },
      {
        id : 4,
        snip: "fdgdia: Ela roubou uma vida. Agora deve pagar com o coração. Acompanhe as aventuras de Feyre pelo perigoso e deslumbrante mundo das fadas. ",
        selected: "",
        book: "Outra coisa ne",
        author: "blz",
        genres: "ficcao"

      },
      {
        id : 5,
        snip: "fdgdia: Ela roubou uma vida. Agora deve pagar com o coração. Acompanhe as aventuras de Feyre pelo perigoso e deslumbrante mundo das fadas. ",
        selected: "",
        book: "Outra coisa ne",
        author: "blz",
        genres: ""

      },
    ]
      
    };
  },
  methods: {
    proximo() {
      if (this.perguntas[this.question_id-1].selected === this.respostas[0].id ){ 
        var g =  this.perguntas[this.question_id-1].genres; //descobrindo o gênero da pergunta
        console.log(this.respostas[0].id)
        var result = this.genres.find(genre => {
        if (genre.name === g) {
          genre.contador += 1
          // console.log(genre.contador)
          // console.log(this.genres[0].contador)
          return result
        } //filtrando os gêneros por nome e adicionando um contador no gênero igual à const g (o gênero da pergunta).
        else {
        }  
      })
      }
      else if (this.perguntas[this.question_id-1].selected === this.respostas[2].id ) {
        var g =  this.perguntas[this.question_id-1].genres; //descobrindo o gênero da pergunta
        // console.log(g)
        console.log(this.respostas[2].id)
        var result = this.genres.find(genre => {
        if (genre.name === g) {

          
          genre.contador -= 1
          // console.log(this.genres[0].contador)
          // console.log(genre.contador)
          return result
        } //filtrando os gêneros por nome e adicionando um contador no gênero igual à const g (o gênero da pergunta).
        else {
        }  
        })
      
      } else {}
      console.log(this.genres[0].contador)
      this.question_id += 1; //adicionando um marcador para trocar de pergunta
    },
    async enviar() {
      try{
            const quizResponse = (await this.$axios.post('/quizz/create', JSON.stringify(this.answer), {headers: {'Content-Type': 'application/json'}})).data
            console.log(quizResponse)
  
          } catch(e) {
              return Promise.reject(e) }
  
    },
  },


  mounted() {
    this.id = this.$router.currentRoute.params.id;
  },
};
</script>

<style scoped lang="scss">
@media (max-width: $phone_l) {
  .card{
    width: 90vw !important;
  }
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
