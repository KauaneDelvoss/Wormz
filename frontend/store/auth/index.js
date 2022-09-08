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
    },
}

export const actions = {
    async LOGIN( { commit }, user){
        try{
            const getFormData = object => Object.keys(object).reduce((formData, key) => {
                formData.append(key, object[key]);
                return formData;
            }, new FormData());

            const userInfo = await this.$authServiceLogin.login(user)
            user.token = userInfo.access
            
            const userResponse = (await this.$axios.post('/get/user', getFormData({'username': user.username }), {headers: {'Content-Type': 'multipart/form-data'}})).data
            user.id = userResponse.id
            user.first_name = userResponse.first_name
            user.last_name = userResponse.last_name

            commit('SET_LOGIN_INFO', user)
            return Promise.resolve(userInfo)
        } catch(e) {
            dispatch('LOGOUT')
            return Promise.reject(e)
        }
    },

    async LOGOUT({commit}){
        commit('SET_LOGOUT')
    },

    SIGN_UP_USER({ commit, dispatch, state }, formData){
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
                    } else {
                        state.user = {}
                        state.loggedIn = false
                    }
                })
            } else {
                alert(response.data)
            }
        })
    }
}