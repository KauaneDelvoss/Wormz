from rest_framework.viewsets import ModelViewSet

from core.models import Own
from core.serializers import OwnSerializer
    
class OwnViewSet(ModelViewSet):
    queryset = Own.objects.all()
    serializer_class = OwnSerializer