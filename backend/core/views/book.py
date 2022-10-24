from rest_framework.viewsets import ModelViewSet

from core.models import Book, Author
from core.serializers import BookSerializer

#from rest_framework.viewsets import ModelViewSet
#from rest_framework.permissions import IsAuthenticated

# from django.contrib.auth.models import AbstractUser as DjangoAuthAdmin
#from django.contrib.auth import get_user_model
#from django.contrib.auth.models import Group
from django.http.response import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render

from core.models import User
from core.serializers import UserSerializer, UserAuthSerializer


class BookViewSet(ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = BookSerializer

    def cadastro(request):
        if request.POST:
            name_book = request.POST.get("name_book")
            resume = request.POST.get("resume")
            pages = request.POST.get("pages")
            #adicionar campo editora do livro
            #adicionar autor

            book = User.objects.filter(name_book=name_book).first() 
            #book = User.objects.filter(name_book=name_book, editora=editora).first() #podem existir várias versões com o mesmo nome

            if book:
                return render(HttpResponse("Já existe um livro com esse nome!"))
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                )
                # id_user = (User.objects.get(username=username)).id
                # perfil = User(username=username, user_biography=user_biography) #, cod_user=id_user)
                user.is_active = True
                user.save()
                # perfil.save()

                # user_group = User.objects.get(username = username)
                # user_group.groups.add(group)

                user.groups.add(group)

                return HttpResponse("Usuário cadastrado com sucesso!")






    
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

