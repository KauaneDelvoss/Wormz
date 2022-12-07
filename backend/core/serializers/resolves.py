from rest_framework.serializers import ModelSerializer

from core.models import Resolves

class ResolvesSerializer(ModelSerializer):
    class Meta:
        model = Resolves
        fields = "__all__"