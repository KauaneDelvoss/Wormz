from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User as UserDjangoAuth
from django.contrib.auth.models import Group
from django.http.response import HttpResponse
from rest_framework.renderers import JSONRenderer

from core.models import User
from core.serializers import UserSerializer

class UserViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def cadastro(request):
        if request.method == "POST" :
            username = request.POST.get('username')
            nickname = request.POST.get('nickname')
            password = request.POST.get('password')
            email = request.POST.get('email')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            user_biography = request.POST.get('user_biography')

            if user:
                return HttpResponse("Já existe um usuário com esse username!")
            else:
                user = UserDjangoAuth.objects.create_user(username = username, password = password, email=email, first_name=first_name, last_name=last_name)
                id_user = (UserDjangoAuth.objects.get(username=username)).id
                perfil = User(nickname=username, user_biography=user_biography, cod_user=id_user)

                user.save()
                perfil.save()

                user_group = UserDjangoAuth.objects.get(username = username)
                user_group.groups.add(group)
                return HttpResponse('Usuário cadastrado com sucesso!')