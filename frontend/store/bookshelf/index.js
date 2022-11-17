export const state = () => ({
    bookshelf: {},
    bookshelves: []
})

export const mutations = {

    SET_BOOKSHELF_INFO(state, payload){
        state.bookshelf = payload
    },

    SET_BOOKSHELVES(state, payload){
        state.bookshelves = payload
    }
}



export const actions = {
    GET_BOOKSHELF({ commit }, bookshelf){
        this.$axios.$get('get/' + bookshelf.user.username + '/bookshelf/' + bookshelf.id).then(
            response => {
                commit("SET_BOOKSHELF_INFO", response)
            }
        )

    },

    GET_BOOKSHELVES({commit}, user_username){
        this.$axios.get('get/' + user_username + '/bookshelf' ).then(
            response => {
                commit("SET_BOOKSHELVES", response.data)
            }
        )
    },

    async ADD_BOOKSHELF( { commit, dispatch }, bookshelf){
        try{
            const bookshelfResponse = (await this.$axios.post('/bookshelf/create', JSON.stringify(bookshelf), {headers: {'Content-Type': 'application/json'}})).data
            console.log(bookshelfResponse)

            dispatch("GET_BOOKSHELVES", bookshelf.user.username)
            
        } catch(e) {
            return Promise.reject(e) }
    },



    ADD_TO_BOOKSHELF({ commit }, payload){

        this.$axios.post('post/addBookshelf', JSON.stringify(payload), {headers: {'Content-Type': 'application/json'}}).then(
            response => {
                console.log(response.data)
            }
        )

    }
}


