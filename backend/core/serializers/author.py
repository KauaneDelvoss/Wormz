from rest_framework.serializers import ModelSerializer

from core.models import Author

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"