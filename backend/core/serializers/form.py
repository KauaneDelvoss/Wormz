from rest_framework.serializers import ModelSerializer

from core.models import Form

class FormSerializer(ModelSerializer):
    class Meta:
        model = Form
        fields = "__all__"