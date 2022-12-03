from rest_framework.viewsets import ModelViewSet

from core.models import Resolves
from core.serializers import ResolvesSerializer


class ResolvesViewSet(ModelViewSet):
    queryset = Resolves.objects.all()
    serializer_class = ResolvesSerializer