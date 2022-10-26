export const state = () => ({
    bookshelf: {}
})

export const actions = {
    GET_BOOKSHELF({ commit }, id){
        this.$axios.post('/bookshelf/get', id).then(
            response => {
                console.log(response)
            }
        )
    }
}


