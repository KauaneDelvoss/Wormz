from rest_framework.renderers import JSONRenderer
import json
from django.http.response import HttpResponse

from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet

from core.models import AnswerAssociativa, User, Answer, Question, Genre, Form, Bookshelf
from core.serializers import AnswerAssociativaSerializer
from core.views import BookshelfViewSet


class AnswerAssociativaViewSet(ModelViewSet):
    queryset = AnswerAssociativa.objects.all()
    serializer_class = AnswerAssociativaSerializer

    def createQuiz(request):
        body = json.loads(request.body.decode('utf-8'))
        print(body)
        cod_answer = body["cod_answer"]
        cod_question = body["cod_question"]
        cod_form = body["cod_forms"]
        user = body["user"]
        print(body)
        user = User.objects.get(pk = user)

        quiz = AnswerAssociativa.objects.create(
                    cod_resp_forms = user,
                    cod_answer = Answer.objects.get(status = cod_answer),
                    cod_question = Question.objects.get(id = cod_question ),
                )
        quiz.cod_forms.add(Form.objects.get(name_forms = cod_form))
        print(quiz)
        quiz.save()

        print(body)
        return HttpResponse(quiz)

    def BookshelfQuiz(request) :
        pass

