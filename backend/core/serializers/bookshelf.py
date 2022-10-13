from rest_framework.serializers import ModelSerializer

from core.models import Bookshelf

class BookshelfSerializer(ModelSerializer):
    class Meta:
        model = Bookshelf
        fields = "__all__"
