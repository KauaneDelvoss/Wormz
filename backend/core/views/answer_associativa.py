from rest_framework.renderers import JSONRenderer
import json
from django.http.response import HttpResponse

from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet

from core.models import AnswerAssociativa, User, Answer, Question, Genre, Form
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
        cod_forms = body["cod_forms"]
        user = body["user"]
        print(body)
        # print(user['id'])
        user = User.objects.get(pk = user)

        # user = User.objects.get(pk = user["id"])
        quiz = AnswerAssociativa.objects.create(
                    cod_resp_forms = user,
                    cod_answer = Answer.objects.get(status = cod_answer),
                    cod_question = Question.objects.get(id = cod_question ),
                    cod_forms = Form.objects.get(id = cod_forms)
                )

        quiz.save()

        print(body)
        return HttpResponse("deu certo?")

    def BookshelfQuiz(request) :
        #filtrar os livros por id e contador
        #chamar pelo id do objeto da answer associativa
        user = User.objects.get(pk = 1)
        cont = 0
        for i in Genre.objects.count():
            if AnswerAssociativa.objects.count(cod_resp_form = 1):
                pass
        

