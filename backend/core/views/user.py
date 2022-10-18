from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

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

            