from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# from django.contrib.auth.models import AbstractUser as DjangoAuthAdmin
import json
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
        
        body = json.loads(request.body)
            
        username = body["username"]
        # nickname = request.POST.get('nickname')
        password = body["password"]
        email = body["email"]
        first_name = body["first_name"]
        last_name = body["last_name"]
        user_biography = body["user_biography"]

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
                user_biography=user_biography
            )
            user.is_active = True
            user.save()

            user.groups.add(group)

            return HttpResponse("Usuário cadastrado com sucesso!")


    def getUser(request):
        body = json.loads(request.body)
        
        user = User.objects.get(username=body["username"])

        serializers = UserAuthSerializer(user)
        data = serializers.data

        data.update(username=user.username)

        jsonn = JSONRenderer().render(data)
        return HttpResponse(jsonn, content_type="text/json-comment-filtered")


    def updateUser(request):
        if request:
            body = json.loads(request.body)
            
            user = User.objects.get(pk = body["id"])
            
            user.user_biography = body["user_biography"]
            user.username = body["username"]
            user.first_name = body["first_name"]
            user.last_name = body["last_name"]
            user.email = body["email"]

            user.save()

            return HttpResponse("Usuário atualizado com sucesso!")
        else:
            return HttpResponse("Algo deu errado.")


    def deleteUser(request):
        body = json.loads(request.body)

        user = User.objects.get(pk=body["id"])
        user.delete()
        
        return HttpResponse("Usuário deletado com sucesso!")
