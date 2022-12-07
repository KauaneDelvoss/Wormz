from rest_framework.viewsets import ModelViewSet

from core.models import Answer
from core.serializers import AnswerSerializer


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer