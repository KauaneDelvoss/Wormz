from rest_framework.serializers import ModelSerializer

from core.models import AnswerAssociativa

class AnswerAssociativaSerializer(ModelSerializer):
    class Meta:
        model = AnswerAssociativa
        fields = "__all__"