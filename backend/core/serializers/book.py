from asyncore import write
from pkg_resources import require
from rest_framework.serializers import ModelSerializer, SlugRelatedField


from core.models import Book
from media.models import Image
from media.serializers import ImageSerializer



class BookSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa", 
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True
    )
    capa = ImageSerializer(required=False, read_only=True)

    class Meta:
            model = Book
            fields = "__all__"
            # depth = 1

#class LivroDetailSerializer(ModelSerializer):
#   capa = ImageSerializer(required=False)
