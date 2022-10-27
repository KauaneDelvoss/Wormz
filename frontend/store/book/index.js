export const state = () => ({
    book: {},
    api_key: 'AIzaSyDb8Cue7PCPcACj9eba6p82EDDLHwXDNLk'
})

export const mutations = {
    COMMIT_URL(state, payload){
        console.log(payload)
        state.book = payload
    },

    SET_BOOK(state, payload){
        console.log(payload)
        state.book = payload
    }
}

export const actions = {
    GET_URL({state, commit}, id){
            const url = 'https://www.googleapis.com/books/v1/volumes/' + id + '?projection=full' + "&key=" + state.api_key
            this.$axios.$get(url, {headers: {
                'Authorization': ''
            }})
            .then(res => { 
                commit('COMMIT_URL',  res)
            })
        },

        GET_BOOK({commit}, id){
            
            this.$axios.$get('/get/book/' + id).then(
                response => {
                    commit("SET_BOOK", response)
                }
            )
        }
    }
