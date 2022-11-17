from rest_framework.viewsets import ModelViewSet
from django.http.response import HttpResponse
#from .bookshelf import Bookshelf
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from yaml import serialize
from core import serializers
from core.models.book import Book
from core.serializers import BookshelfSerializer
import json


from core.models import Bookshelf, Book, User
from core.serializers import BookshelfSerializer, BookSerializer

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
        
        
        print(user_username, id)
        print((Bookshelf.objects.get(id)).book)
        print(Book.objects.filter(pk = (Bookshelf.objects.get(id)).book))
        

    def addBookshelf(request):
        
        if request.POST:
            body = request.body
            book = Book.objects.get(pk = body["id_book"])

            for item in body["bookshelves"]:
                bookshelf = Bookshelf.objects.get(pk = item["id"])
                bookshelf.add(book)

            return HttpResponse("Estantes atualizadas com sucesso!")
        
        else:
            return HttpResponse("Método proibido: somente POST")
    

    def removeBookshelf():
        pass


    def deleteBookshelf(request):
        
        bookshelf = Bookshelf.objects.get(pk=request.POST.get("id"))
        bookshelf.delete()
        return HttpResponse("Estante deletada com sucesso!")
