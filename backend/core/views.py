from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User as UserDjangoAuth
from django.contrib.auth.models import Group
from django.http.response import HttpResponse

from core.models import User
from core.serializers import UserSerializer

class UserViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

def cadastro(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        group = Group.objects.get(name='common_users') 
        user = UserDjangoAuth.objects.filter(username=username).first()
        
        if user:
            return HttpResponse("Já existe um usuário com esse username!")
        else:
            user = UserDjangoAuth.objects.create_user(username = username, password = password, email=email, first_name=first_name, last_name=last_name)
            user.save()

            user_group = UserDjangoAuth.objects.get(username = username)
            print(user_group)
            print(group)
            user_group.groups.add(group)
            return HttpResponse('Usuário cadastrado com sucesso!')