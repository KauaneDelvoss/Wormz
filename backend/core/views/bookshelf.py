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
        if request.POST:
            bookshelf_name = request.POST.get("bookshelf_name")
            # nickname = request.POST.get('nickname')
            bookshelf_desc = request.POST.get("bookshelf")
            user = request.POST.get("user")

            bookshelf = Bookshelf.objects.filter(bookshelf_name=bookshelf_name).first()

            print(request.POST)
            if bookshelf:
                return HttpResponse("Já existe uma estante com esse nome!")
            else:
                bookshelf = Bookshelf.objects.create(
                    bookshelf_name=bookshelf_name,
                    booshelf_desc=bookshelf_desc,
                    user = User.objects.get(pk = user)
                    #email=email,
                    #first_name=first_name,
                    #last_name=last_name,
                )
                
                bookshelf.save()
           

                # user_group = User.objects.get(username = username)
                # user_group.groups.add(group)

                #user.groups.add(group)

                return HttpResponse("Estante cadastrado com sucesso!")

    def getBookshelves(request, user_username):
        user_id = User.objects.get(username = user_username).id
        bookshelves = (Bookshelf.objects.filter(user = user_id)).values()

        # serializers = BookshelfSerializer(i)
        # data = serializers.data
        # json =  JSONRenderer().render(data)

        data = list(bookshelves)  # wrap in list(), because QuerySet is not JSON serializable
        return JsonResponse(data, safe=False)  # or JsonResponse({'data': data})


    def getBookshelf(request, user_username, id):
        # username = request.POST.get("username")

        user = User.objects.get(username = user_username)
        book_serializer = BookSerializer(Book.objects.get(bookshelf = id))
        serialize = book_serializer.data

        bookshelf = (Bookshelf.objects.filter(user = user, pk=id)).values()
        bookshelf = list(bookshelf)

        data = {}

        data.update(book = serialize, bookshelf_info = bookshelf[0])

        # data = list(data)  # wrap in list(), because QuerySet is not JSON serializable

        # return JsonResponse(data, safe=False)  # or JsonResponse({'data': data})

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