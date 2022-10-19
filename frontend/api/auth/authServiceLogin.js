export default async function ( { app: { $axios }}, inject ) {
        inject("authServiceLogin", {
                async login(user){
                        const { data } = await $axios.post('/token/', user)
                        return data
                }
        })

 }