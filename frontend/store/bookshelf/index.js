export const state = () => ({
    bookshelf: {}
})

export const mutations = {

    SET_BOOKSHELF_INFO(state){
        state.bookshelf_name = {}
        state.bookshelf_desc = {}
    }
}



export const actions = {
    GET_BOOKSHELF({ commit }, id){
        this.$axios.post('/get/bookshelf/', id).then(
            response => {
                console.log(response)
            }
        )

    },

    async LOGIN( { commit }, bookshelf){
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

            commit('SET_BOOKSHELF_INFO', bookshelf)
            
        } catch(e) {
            return Promise.reject(e) }
    },



    POST_BOOKSHELF({commit, dispatch}, formData) {
        const getFormData = object => Object.keys(object).reduce((formData, key) => {
            formData.append(key, object[key]);
            return formData;
        }, new FormData());

        console.log(formData)
        this.$axios.post('/get/bookshelf/', getFormData(formData),
        {headers: {'Content-Type': 'multipart/form-data'}})
        .then(response => {
            if(response.status == 200){
                dispatch('LOGIN', { "bookshelf_name": formData.bookshelf_name, "bookshelf_desc": formData.bookshelf_desc }).then(response => {
                    if(response){
                        commit('SET_BOOKSHELF_INFO')
                    } else {
                        alert(response.data)
                    }
                })
            } else {
                alert(response.data)
            }
        })
    }
}


