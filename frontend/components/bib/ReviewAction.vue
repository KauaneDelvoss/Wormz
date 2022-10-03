<template>
  <div class="review-action">
    <v-card outlined height="15vh" width="50vw" class="card-container">
        <div class="d-flex margin-left-page margin-right-page">
            <v-text-field
                style="width: 70%"
                dark
                color="#E8E5AE"
                v-model="review.text"
                label="Review"
            ></v-text-field>
        </div>
    </v-card>
  </div>
</template>

<script>
export default {
    data(){
        return{
            review: {}
        }
    }
}
</script>

<style scoped lang="scss">

.card-container{
    background-color: variables.$bg-color !important;
}
</style>