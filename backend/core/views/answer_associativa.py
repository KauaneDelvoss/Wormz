from rest_framework.renderers import JSONRenderer
import json
from django.http.response import HttpResponse

from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet

from core.models import AnswerAssociativa, User, Answer, Question, Genre, Form, Bookshelf
from core.serializers import AnswerAssociativaSerializer, UserSerializer
from core.views import BookshelfViewSet


class AnswerAssociativaViewSet(ModelViewSet):
    queryset = AnswerAssociativa.objects.all()
    serializer_class = AnswerAssociativaSerializer

    def createQuiz(request):
        body = json.loads(request.body.decode('utf-8'))
        # print(body)
        cod_answer = body["cod_answer"]
        cod_question = body["cod_question"]
        cod_form = body["cod_forms"]
        user = body["user"]
        # print(body)
        user = User.objects.get(pk = user)

        quiz = AnswerAssociativa.objects.create(
                    cod_resp_forms = user,
                    cod_answer = Answer.objects.get(status = cod_answer),
                    cod_question = Question.objects.get(id = cod_question ),
                )
        quiz.cod_forms.add(Form.objects.get(name_forms = cod_form))
        # print(quiz)
        quiz.save()

        
        # print(body)
        return HttpResponse(quiz)

    def BookshelfQuiz(request) :
        body = json.loads(request.body.decode('utf-8'))
        bookshelf_name = 'Estante com livros indicados' 
        bookshelf_desc = 'Estante com livros indicados'
        user = body["user"]
        users = User.objects.get(pk = user)

        serializer = UserSerializer(users).data
        # print(users.first_name)

        info = {'bookshelf_name' : bookshelf_name , 'bookshelf_desc' : bookshelf_desc, 'user':  {'username': serializer['username'], 'password': serializer['password'], 'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcwNTE4NTMyLCJpYXQiOjE2NzA1MTgyMzIsImp0aSI6IjFkZjc1ZTYzM2Y3MjRiYzE5YTQ3NTBjNjY4MTM5ZjBlIiwidXNlcl9pZCI6MX0.QIiaIvvFb-7ZGIxwxakE7zULyieFk3Z8-zx4S_0VZlQ', 'id': serializer['id'], 'first_name': serializer['first_name'], 'last_name': serializer['last_name']}}
        # print(info)

        BookshelfViewSet.createBookshelfQuiz(json.dumps(info))


        return HttpResponse("oi") 
        # return HttpResponse(request)







