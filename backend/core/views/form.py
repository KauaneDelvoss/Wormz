from rest_framework.viewsets import ModelViewSet

from core.models import Form
from core.serializers import FormSerializer


class FormViewSet(ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer