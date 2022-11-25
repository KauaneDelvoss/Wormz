from rest_framework.serializers import ModelSerializer

from core.models import Review

class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"