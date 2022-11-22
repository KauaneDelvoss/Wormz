from rest_framework.viewsets import ModelViewSet
from django.http.response import HttpResponse
#from .bookshelf import Bookshelf
from rest_framework.renderers import JSONRenderer
import json
from django.http import JsonResponse
from yaml import serialize
from core import serializers
from core.models.book import Book
from core.serializers import BookshelfSerializer, BookSerializer

from core.models import User
from core.models import Bookshelf, bookshelf
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

            bookshelf = Bookshelf.objects.filter(bookshelf_name=bookshelf_name).first()

            if bookshelf:
                return HttpResponse("Já existe uma estante com esse nome!")
            else:
                bookshelf = Bookshelf.objects.create(
                    bookshelf_name=bookshelf_name,
                    booshelf_desc=bookshelf_desc,
                    user = user
                )

                bookshelf.save()

                return HttpResponse("Estante cadastrada com sucesso!")

        else:
            return HttpResponse("Algo deu errado.")

    def getBookshelves(request, user_username):
        user_id = User.objects.get(username = user_username).id
        bookshelves = (Bookshelf.objects.filter(user = user_id)).values()

        data = list(bookshelves)  
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

        book = Book.objects.get(pk = body["id_book"])

        for item in body["bookshelves"]:
            bookshelf = Bookshelf.objects.get(pk = item["id"])
            bookshelf.book.add(book)

        return HttpResponse("Estantes atualizadas com sucesso!")
        

    def removeBookshelf():
        pass




    def deleteBookshelf():
        pass