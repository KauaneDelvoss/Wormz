from rest_framework.viewsets import ModelViewSet

from core.models import Book, Author, Genre
from core.serializers import BookSerializer, AuthorSerializer

from django.http.response import HttpResponse
from rest_framework.renderers import JSONRenderer


class BookViewSet(ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def cadastro(request):
        if request.POST:
            name_book = request.POST.get("name_book")
            resume = request.POST.get("resume")
            pages = request.POST.get("pages")
            #adicionar campo editora do livro
            #adicionar autor

            book = Book.objects.filter(name_book=name_book).first() 
            #book = User.objects.filter(name_book=name_book, editora=editora).first() #podem existir várias versões com o mesmo nome

            if book:
                return HttpResponse("Já existe um livro com esse nome!")
            else:
                book = Book.objects.create(
                    name_book=name_book,
                    resume=resume,
                    pages=pages,
                    #editora = editora,
                    
                )
                # id_user = (User.objects.get(username=username)).id
                # perfil = User(username=username, user_biography=user_biography) #, cod_user=id_user)
                #user.is_active = True
                book.save()
                # perfil.save()

                # user_group = User.objects.get(username = username)
                # user_group.groups.add(group)

                #user.groups.add(group)

                return HttpResponse("Livro cadastrado com sucesso!")


    def getBook(request, id):
        # username = request.POST.get("username")
        book = Book.objects.get(pk = id)
        # perfil = User.objects.get(username = username)

        serializers = BookSerializer(book)
        data = serializers.data
        
        author = []
        for item in data["author"]:
            author.append(Author.objects.get(pk = item).name_author)
        data["author"] = author

        genre = []
        for item in data["genre"]:
            genre.append(Genre.objects.get(pk = item).name_genre)
        data["genre"] = genre

        json = JSONRenderer().render(data)
        return HttpResponse(json, content_type="text/json-comment-filtered")

    def getSearch(request, search):
        author = Author.objects.filter(name_author__icontains = search)
        author_serializer = (AuthorSerializer(author, many=True)).data
        # jsonAuthor = JSONRenderer().render(author_serializer)
        
        book = Book.objects.filter(name_book__icontains = search)

        serializers = BookSerializer(book, many=True)
        data = serializers.data
        
        # for item in jsonAuthor:
        #     books_in_author = Book.objects.filter(author = item.id) # tem que entrar num for
        #     print(books_in_author)
            
        # data.append(books_in_author)
        
        json = JSONRenderer().render(data)
        
        
        return HttpResponse(json, content_type="text/json-comment-filtered")

