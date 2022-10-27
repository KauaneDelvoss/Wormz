from rest_framework.viewsets import ModelViewSet
from django.http.response import HttpResponse
#from .bookshelf import Bookshelf
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from yaml import serialize
from core import serializers
from core.models.book import Book
from core.serializers import BookshelfSerializer

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
        print(user_username, id)
        print((Bookshelf.objects.get(id)).book)
        print(Book.objects.filter(pk = (Bookshelf.objects.get(id)).book))
        #print(request.POST)
        #return HttpResponse("uhum")

        
        #bookshelf = Bookshelf.objects.get(bookshelf_name=request.POST.get("Bookshelf.id"))
        # bookshelf = Bookshelf.objects.get(pk = request.POST.get(id))
        #livros que estão dentro dela

        # serializers = BookshelfSerializer(bookshelf)
        # data = serializers.data

        # data.update(bookshelf_name=bookshelf.bookshelf_name)

        # json = JSONRenderer().render(data)
        # #json
        # return HttpResponse(json, content_type="text/json-comment-filtered")

    def addBookshelf():
        pass
        #id livro
        #if bookshelf
    

    def removeBookshelf():
        pass




    def deleteBookshelf():
        pass