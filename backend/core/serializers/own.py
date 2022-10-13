from rest_framework.serializers import ModelSerializer

from core.models import Own

class OwnSerializer(ModelSerializer):
    class Meta:
        model = Own
        fields = "__all__"
