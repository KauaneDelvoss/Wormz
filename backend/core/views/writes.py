from rest_framework.viewsets import ModelViewSet

from core.models import Writes
from core.serializers import WritesSerializer
    
class WritesViewSet(ModelViewSet):
    queryset = Writes.objects.all()
    serializer_class = WritesSerializer
    
