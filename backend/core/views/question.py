from rest_framework.viewsets import ModelViewSet

from core.models import Question
from core.serializers import QuestionSerializer


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer