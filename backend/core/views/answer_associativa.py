from rest_framework.renderers import JSONRenderer
import json
from django.http.response import HttpResponse

from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet

from core.models import AnswerAssociativa, User
from core.serializers import AnswerAssociativaSerializer


class AnswerAssociativaViewSet(ModelViewSet):
    queryset = AnswerAssociativa.objects.all()
    serializer_class = AnswerAssociativaSerializer

    def createQuiz(request):
        body = json.loads(request.body.decode('utf-8'))


        print(body)
        # cod_resp_forms = body[]
        cod_answer = body["cod_answer"]
        cod_question = body["cod_question"]
        user = body["user"]

        # print(user['id'])
        user = User.objects.get(pk = user)
        # user = User.objects.get(pk = user["id"])
        quiz = AnswerAssociativa.objects.create(
                    cod_resp_forms = user,
                    cod_answer = cod_answer,
                    cod_question = cod_question
                )

        quiz.save()

        print(body)
        return HttpResponse("deu certo?")