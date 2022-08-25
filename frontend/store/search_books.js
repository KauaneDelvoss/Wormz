// search_books.js

export const state = () => ({
    books: [
        {id: 0, name: "Sagarana", author: "João Guimarães Rosa", date: "1946", review: "4.5", lang: "Português", genre: "Vida sertaneja", type: "Coleção de Contos", href: "https://images-na.ssl-images-amazon.com/images/I/9116siz6Y0L.jpg", liked: true},
        {id: 1, name: "Sagarana", author: "João Guimarães Rosa", date: "1946", review: "4.5", lang: "Português", genre: "Vida sertaneja", type: "Coleção de Contos", href: "https://images-na.ssl-images-amazon.com/images/I/9116siz6Y0L.jpg", liked: true},
        {id: 2, name: "Sagarana", author: "João Guimarães Rosa", date: "1946", review: "4.5", lang: "Português", genre: "Vida sertaneja", type: "Coleção de Contos", href: "https://images-na.ssl-images-amazon.com/images/I/9116siz6Y0L.jpg", liked: false},
        {id: 3, name: "Sagarana", author: "João Guimarães Rosa", date: "1946", review: "4.5", lang: "Português", genre: "Vida sertaneja", type: "Coleção de Contos", href: "https://images-na.ssl-images-amazon.com/images/I/9116siz6Y0L.jpg", liked: true},
        {id: 4, name: "Sagarana", author: "João Guimarães Rosa", date: "1946", review: "4.5", lang: "Português", genre: "Vida sertaneja", type: "Coleção de Contos", href: "https://images-na.ssl-images-amazon.com/images/I/9116siz6Y0L.jpg", liked: false},
        {id: 5, name: "Sagarana", author: "João Guimarães Rosa", date: "1946", review: "4.5", lang: "Português", genre: "Vida sertaneja", type: "Coleção de Contos", href: "https://images-na.ssl-images-amazon.com/images/I/9116siz6Y0L.jpg", liked: false},
        {id: 6, name: "Sagarana", author: "João Guimarães Rosa", date: "1946", review: "4.5", lang: "Português", genre: "Vida sertaneja", type: "Coleção de Contos", href: "https://images-na.ssl-images-amazon.com/images/I/9116siz6Y0L.jpg", liked: true},
    
    ]
        
})

export const mutations = { 
    LIKE_BOOK(state, payload){
        state.books[payload].liked = !state.books[payload].liked
    }
}

export const actions = {
}

export const getters = {
}