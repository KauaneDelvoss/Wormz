export const state = () => ({
    loggedIn: false,
    user: {}
})

export const mutations = {
    INITIALIZE_STORE(state){
        if(process.client){
            if(localStorage.getItem('token')){
                state.user.token = localStorage.getItem('token')
                state.loggedIn = true
            }
        } else {
            state.user = {}
            state.loggedIn = false
        }

        if(state.user.token){
            this.$axios.defaults.headers.common['Authorization'] = 'Bearer ' + state.user.token
        } else {
            this.$axios.defaults.headers.common['Authorization'] = ''
        }
    },
    SET_LOGIN_INFO(state, user){
        state.user = user
        state.loggedIn = true
        if(process.client){
            localStorage.setItem("token", user.token)
        }
    },
    SET_LOGOUT(state){
        state.user = {}
        state.loggedIn = false
        if(process.client){
            localStorage.clear()
        }
    }
}

export const actions = {
    async LOGIN( { commit }, user){
        try{
            const userInfo = await this.$authServiceLogin.login(user)
            user.token = userInfo.access
            commit('SET_LOGIN_INFO', user)
            return Promise.resolve(userInfo)
        } catch(e) {
            commit('SET_LOGOUT')
            return Promise.reject(e)
        }
    },

    LOGOUT({commit}){
        commit('SET_LOGOUT')
    },

    SIGN_UP_USER({commit, dispatch}, formData, formUser){
        const getFormData = object => Object.keys(object).reduce((formData, key) => {
            formData.append(key, object[key]);
            return formData;
        }, new FormData());

        console.log(formData)
        this.$axios.post('/cadastro/', getFormData(formData),
        {headers: {'Content-Type': 'multipart/form-data'}})
        .then(response => {
            if(response.status == 200){
                dispatch('LOGIN', { "username": formData.username, "password": formData.password }).then(response => {
                    if(response){
                        commit('INITIALIZE_STORE')
                        dispatch('SIGN_UP_BIO', formUser)
                    }
                })
            } else {
                alert(response.data)
            }
        })

    },

    SIGN_UP_BIO(formUser){
        this.$axios.post('/users/', formUser).then(response => {
            console.log(response)
        })
    }
}