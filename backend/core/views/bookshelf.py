from rest_framework.viewsets import ModelViewSet
from django.http.response import HttpResponse
#from .bookshelf import Bookshelf
from rest_framework.renderers import JSONRenderer
from core.serializers import BookshelfSerializer


from core.models import Bookshelf, bookshelf
from core.serializers import BookshelfSerializer

class BookshelfViewSet(ModelViewSet):
    queryset = Bookshelf.objects.all()
    serializer_class = BookshelfSerializer

    def cadastro(request):
        if request.POST:
            bookshelf_name = request.POST.get("bookshelf_name")
            # nickname = request.POST.get('nickname')
            booshelf_desc = request.POST.get("bookshelf")
            bookshelf = Bookshelf.objects.filter(bookshelf_name=bookshelf_name).first()


            if bookshelf:
                return HttpResponse("Já existe uma estante com esse nome!")
            else:
                bookshelf = Bookshelf.objects.create_user(
                    bookshelf_name=bookshelf_name,
                    booshelf_desc=booshelf_desc
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

        print(request.POST)
        return HttpResponse("uhum")

        # bookshelf = Bookshelf.objects.get(bookshelf_name=request.POST.get("Bookshelf.id"))
        # perfil = User.objects.get(username = username)

        # serializers = BookshelfSerializer(bookshelf)
        # data = serializers.data

        # data.update(bookshelf_name=bookshelf.bookshelf_name)

        # json = JSONRenderer().render(data)
        # return HttpResponse(json, content_type="text/json-comment-filtered")

    