from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# from django.contrib.auth.models import AbstractUser as DjangoAuthAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.http.response import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render

from core.models import User
from core.serializers import UserSerializer, UserAuthSerializer

# User = get_user_model()


class UserViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def cadastro(request):
        if request.POST:
            username = request.POST.get("username")
            # nickname = request.POST.get('nickname')
            password = request.POST.get("password")
            email = request.POST.get("email")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            user_biography = request.POST.get("user_biography")

            group = Group.objects.get(name="common_users")
            user = User.objects.filter(username=username).first()

            if user:
                return render(HttpResponse("Já existe um usuário com esse username!"))
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

    def getUser(request):
        # username = request.POST.get("username")
        user = User.objects.get(username=request.POST.get("username"))
        # perfil = User.objects.get(username = username)

        serializers = UserAuthSerializer(user)
        data = serializers.data

        data.update(username=user.username)

        json = JSONRenderer().render(data)
        return HttpResponse(json, content_type="text/json-comment-filtered")

    def updateUser(request):
        if request.POST:
            user = User.objects.get(pk = request.POST.get('id'))
            # profile = User.objects.get(cod_user=request.POST.get('id'))
            user.user_biography = request.POST.get("user_biography")
            user.username = request.POST.get("username")
            user.first_name = request.POST.get("first_name")
            user.last_name = request.POST.get("last_name")
            user.email = request.POST.get("email")

            # profile.save()
            user.save()

            return HttpResponse("Usuário atualizado com sucesso!")
        else:
            return HttpResponse("Métodos permitidos: /POST/")

    def deleteUser(request):
        print(request)

        user = User.objects.get(pk=request.POST.get("id"))
        #profile = User.objects.get(cod_user=request.POST.get("id"))
        user.delete()
        #profile.delete()
        return HttpResponse("Usuário deletado com sucesso!")
