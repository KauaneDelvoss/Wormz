from rest_framework.viewsets import ModelViewSet

from core.models import Bookshelf
from core.serializers import BookshelfSerializer

class BookshelfViewSet(ModelViewSet):
    queryset = Bookshelf.objects.all()
    serializer_class = BookshelfSerializer