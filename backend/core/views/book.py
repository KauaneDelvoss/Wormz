from rest_framework.viewsets import ModelViewSet

from core.models import Book
from core.serializers import BookSerializer

#from rest_framework.viewsets import ModelViewSet
#from rest_framework.permissions import IsAuthenticated

# from django.contrib.auth.models import AbstractUser as DjangoAuthAdmin
#from django.contrib.auth import get_user_model
#from django.contrib.auth.models import Group
from django.http.response import HttpResponse
from rest_framework.renderers import JSONRenderer
#from django.shortcuts import render


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


    def getBook(request):
        # username = request.POST.get("username")
        book = Book.objects.get(name_book=request.POST.get("name_book"))
        # perfil = User.objects.get(username = username)

        serializers = BookSerializer(book)
        data = serializers.data

        data.update(username=book.name_book)

        json = JSONRenderer().render(data)
        return HttpResponse(json, content_type="text/json-comment-filtered")