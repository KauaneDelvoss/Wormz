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
    GET_BOOKSHELF({ commit }, id){
        this.$axios.$get('/bookshelf/' + id).then(
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
            const getFormData = object => Object.keys(object).reduce((formData, key) => {
                formData.append(key, object[key]);
                return formData;
            }, new FormData());
            
            console.log(bookshelf)
            const bookshelfResponse = (await this.$axios.post('/bookshelf/create', getFormData(bookshelf), {headers: {'Content-Type': 'multipart/form-data'}})).data
            // bookshelf.id = bookshelfResponse.id
            // bookshelf.bookshelf_name = bookshelfResponse.bookshelf_name
            // bookshelf.bookshelf_desc = bookshelfResponse.booskhelf_desc
            
            commit('GET_BOOKSHELVES', )

            
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


