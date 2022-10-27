from rest_framework.viewsets import ModelViewSet
from django.http.response import HttpResponse
#from .bookshelf import Bookshelf
from rest_framework.renderers import JSONRenderer
from core.serializers import BookshelfSerializer


from core.models import Bookshelf, Book
from core.serializers import BookshelfSerializer, BookSerializer

class BookshelfViewSet(ModelViewSet):
    queryset = Bookshelf.objects.all()
    serializer_class = BookshelfSerializer

    def createBookshelf(request):
        if request.POST:
            bookshelf_name = request.POST.get("bookshelf_name")
            # nickname = request.POST.get('nickname')
            bookshelf_desc = request.POST.get("bookshelf")
            bookshelf = Bookshelf.objects.filter(bookshelf_name=bookshelf_name).first()

            print(request.POST)
            if bookshelf:
                return HttpResponse("Já existe uma estante com esse nome!")
            else:
                bookshelf = Bookshelf.objects.create(
                    bookshelf_name=bookshelf_name,
                    booshelf_desc=bookshelf_desc
                    #email=email,
                    #first_name=first_name,
                    #last_name=last_name,
                )
                
                bookshelf.save()
           

                # user_group = User.objects.get(username = username)
                # user_group.groups.add(group)

                #user.groups.add(group)

                return HttpResponse("Estante cadastrado com sucesso!")

    def getBookshelf(request):
        # username = request.POST.get("username")

        #print(request.POST)
        #return HttpResponse("uhum")

        #bookshelf = Bookshelf.objects.get(bookshelf_name=request.POST.get("Bookshelf.id"))
        bookshelf = Bookshelf.objects.get(pk=request.bookshelf.id)
        #livros que estão dentro dela

        serializers = BookshelfSerializer(bookshelf)
        data = serializers.data

        data.update(pk=bookshelf.bookshelf_name)

        json = JSONRenderer().render(data)
        #json
        print(request.POST)

        return HttpResponse(json, content_type="text/json-comment-filtered")

    def addBookshelf(request, user_username, id):
        #pass
        #id livro
        #id bookshelf   
        pass
        




    

    def removeBookshelf():
        pass




    def deleteBookshelf(request):
        
        bookshelf = Bookshelf.objects.get(pk=request.POST.get("id"))
        bookshelf.delete()
        return HttpResponse("Estante deletada com sucesso!")
