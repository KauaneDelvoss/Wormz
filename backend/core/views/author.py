from rest_framework.viewsets import ModelViewSet

from core.models import Author
from core.serializers import AuthorSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer