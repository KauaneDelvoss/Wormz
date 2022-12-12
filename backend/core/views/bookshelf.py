from rest_framework.viewsets import ModelViewSet
from django.http.response import HttpResponse
#from .bookshelf import Bookshelf
from rest_framework.renderers import JSONRenderer
import json
from django.http import JsonResponse
from yaml import serialize
from core import serializers
from core.models import Book, AnswerAssociativa
from media.models.image import Image
from core.serializers import BookshelfSerializer, BookSerializer
from media.serializers import ImageSerializer
import random
# from core.views import AnswerAssociativaViewSet

from core.models import User
from core.models import Bookshelf, Question, Genre
from core.serializers import BookshelfSerializer

class BookshelfViewSet(ModelViewSet):
    queryset = Bookshelf.objects.all()
    serializer_class = BookshelfSerializer

    def createBookshelf(request):
        if request.body:
            body = json.loads(request.body.decode('utf-8'))

            print(body)

            bookshelf_name = body["bookshelf_name"]
            bookshelf_desc = body["bookshelf_desc"]
            user = body["user"]

            user = User.objects.get(pk = user["id"])

            # bookshelf = Bookshelf.objects.filter(bookshelf_name=bookshelf_name).first()
        

            bookshelf = Bookshelf.objects.create(
                bookshelf_name=bookshelf_name,
                booshelf_desc=bookshelf_desc,
                user = user
            )

            bookshelf.save()

            return HttpResponse("Estante cadastrada com sucesso!")

        # elif request:
            
        #     body = json.loads(request)

        #     print(body)

        #     bookshelf_name = body["bookshelf_name"]
        #     bookshelf_desc = body["bookshelf_desc"]
        #     user = body["user"]

        #     user = User.objects.get(pk = user["id"])

        #         # bookshelf = Bookshelf.objects.filter(bookshelf_name=bookshelf_name).first()
            

        #     bookshelf = Bookshelf.objects.create(
        #         bookshelf_name=bookshelf_name,
        #         booshelf_desc=bookshelf_desc,
        #         user = user
        #         )

        #     bookshelf.save()

        #     return HttpResponse("Estante cadastrada com sucesso!")

    def createBookshelfQuiz(request):
        if request:
            body = json.loads(request)

            # print(body)

            bookshelf_name = body["bookshelf_name"]
            bookshelf_desc = body["bookshelf_desc"]
            user = body["user"]

            user = User.objects.get(pk = user["id"])
            bookshelf = Bookshelf.objects.filter(bookshelf_name=bookshelf_name).first() 
            # bookshelf = Bookshelf.objects.filter(bookshelf_name=bookshelf_name).first()
        

            if bookshelf:
                bookshelf_name=bookshelf_name,
                bookshelf_desc=bookshelf_desc,
                user = user
                bookshelf.save()
            else:
                bookshelf = Bookshelf.objects.create(
                bookshelf_name=bookshelf_name,
                booshelf_desc=bookshelf_desc,
                user = user
                )
                # id_user = (User.objects.get(username=username)).id
                # perfil = User(username=username, user_biography=user_biography) #, cod_user=id_user)
                #user.is_active = True
                bookshelf.save()

        
        c = AnswerAssociativa.objects.filter(cod_resp_forms = user, cod_forms = 1 )
        genre = Question.objects.filter(id = 1).prefetch_related('genres').all #sera que não estou usando na entidade errada? Sim eu estava, tenho que puxar esse atributo da entidade que eu o atribui
        count_genre = Genre.objects.all()
        count_question = Question.objects.all()
        # print(genre)
        # print(count_genre)
        # print(genre(1).genres)
        # a = Question.objects.all()
        # print(c[0].cod_question)
        # print(count_question[0].text)

        # lista = []
        # ordens = Question.objects.all()
        # for ordem in ordens:
        #     for o in ordem.genres.all():
        #         lista.append(o.genres)
        # print(lista[0])

        # print(count_question[0].genres)


        # for i in range(c.count()): #para cada elemento dos formulários associativos 
        #     # 
        #     # print(c[i].id) #mostrar o id elemento
        #     for ii in range(count_genre.count()): #para cada item em questões
        #         # print(count_genre[ii])
        #         for iii in range(count_question.count()):
        #             if str(c[i].cod_question) == str(count_question[iii].text):
        #                 #tenho que descobrir aqui o gênero da questão


        #                 print(count_question[iii].text )
        #             else :
        #                 print()
                # if c[i].cod_question == a[ii]: #tenho que igualar o gênero da questão
            #         print(genre[ii].genres) #ver se o código da questão bate com o código do item das questões
            #         for iii in range(1,4):
            #             if c[i].cod_answer == iii:
            #                 continue





        info = {'bookshelf_name' : bookshelf_name, 'bookshelf_desc' : bookshelf_desc, 'id' : 35 , 'user_id' : user.id }
        # print(info)
        BookshelfViewSet.addBookshelfQuiz(json.dumps(info))
        return HttpResponse("Estante cadastrada com sucesso!")

        # bookshelf_name
        # : 
        # "Estante com livros indicados"
        # booshelf_desc
        # : 
        # "Estante com livros indicados"
        # id
        # : 
        # 35
        # user_id
        # : 
        # 1


    def getBookshelves(request, user_username):
        user_id = User.objects.get(username = user_username).id
        bookshelves = (Bookshelf.objects.filter(user = user_id)).values()
        data = list(bookshelves)  

        for item in data:
            books = BookSerializer(Book.objects.filter(bookshelf = item["id"]), many=True).data
            item.update(book = books)

        return JsonResponse(data, safe=False) 


    def getBookshelf(request, user_username, id):
        # username = request.POST.get("username")
        book_serializer = []
        user = User.objects.get(username = user_username)
        
        count = Book.objects.filter(bookshelf = id)

        bookshelf = (Bookshelf.objects.filter(user = user, pk=id)).values()
        bookshelf = list(bookshelf)
        data = {}

        if len(count) > 0:
            for item in count:
                book_serializer.append(BookSerializer(item).data)

            data.update(book = book_serializer, bookshelf_info = bookshelf[0])
        
        else:
            data.update(book = {}, bookshelf_info = bookshelf[0])

        json = JSONRenderer().render(data)
        return HttpResponse(json, content_type="text/json-comment-filtered")
    

    def addBookshelf(request):
        body = json.loads(request.body)
        # print(body)
        book = Book.objects.get(pk = body["id_book"])
        print(body["bookshelves"])

        for item in body["bookshelves"]:
            # print(item)
            bookshelf = Bookshelf.objects.get(pk = item["id"])
            bookshelf.book.add(book)

        return HttpResponse("Estantes atualizadas com sucesso!")
        
    def addBookshelfQuiz(request):
        body = json.loads(request)
        # print(body)
        bookshelves = []

        # 1. tenho que pegar informações das estantes do usuário
        # for i in bookshelf
        bookshelf = Bookshelf.objects.filter(user = 1)
        for i in range(0,bookshelf.count()):
            serializer = BookshelfSerializer(bookshelf[i]).data
            bookshelves.append(serializer)
         
        # print(bookshelves)
        #  
        for i in range(1,4): #escolher a quantidade de livros que vai na bookshelf recém criada
            # a = random.randrange(20) -> criar um contador aleatório para os livros para substituir id
            

            book = Book.objects.get(pk = i)
            genre_books = Book.objects.prefetch_related('genre').filter(genre = 2) #Puxar o gênero escolhido no campo genre = x
            # print(genre_books)
            # print(book)
            # print(genre_books.count())
            for a in range(0,genre_books.count()):
                if (book == genre_books[a]): 
                    # print("oi")
                    for item in bookshelves:
                        bookshelf = Bookshelf.objects.get(pk = item["id"])
                        bookshelf.book.add(book)
                        # print(item)
                else: 
                    print("o que?")
        return HttpResponse("Estantes atualizadas com sucesso!")
        

    def editBookshelf(request):
        body = json.loads(request.body)
        bookshelf = Bookshelf.objects.get(pk = body["id"])
        bookshelf.bookshelf_name = body["bookshelf_name"]
        bookshelf.booshelf_desc = body["bookshelf_desc"]
        bookshelf.save()

        return HttpResponse("Estante atualizada com sucesso!")


    def deleteBookshelf(request, id):
        bookshelf = Bookshelf.objects.get(pk = id)
        bookshelf.delete()

        return HttpResponse("Estante deletada com sucesso!")