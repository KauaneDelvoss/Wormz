from rest_framework.viewsets import ModelViewSet

from core.models import Type
from core.serializers import TypeSerializer

class TypeViewSet(ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    