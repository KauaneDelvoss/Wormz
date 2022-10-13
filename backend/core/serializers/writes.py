from rest_framework.serializers import ModelSerializer

from core.models import Writes

class WritesSerializer(ModelSerializer):
    class Meta:
        model = Writes
        fields = "__all__"
