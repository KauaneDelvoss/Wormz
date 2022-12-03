from rest_framework.viewsets import ModelViewSet

from core.models import AnswerAssociativa
from core.serializers import AnswerAssociativaSerializer


class AnswerAssociativaViewSet(ModelViewSet):
    queryset = AnswerAssociativa.objects.all()
    serializer_class = AnswerAssociativaSerializer