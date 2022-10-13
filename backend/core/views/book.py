from rest_framework.viewsets import ModelViewSet

from core.models import Book
from core.serializers import BookSerializer
    
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer