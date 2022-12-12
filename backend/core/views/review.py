from rest_framework.viewsets import ModelViewSet
from django.http.response import HttpResponse
from django.http import JsonResponse

from core.models.review import Review, User, Book
from core.serializers import ReviewSerializer
from rest_framework.renderers import JSONRenderer

import json

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def submitReview(request):
        body = json.loads(request.body.decode('utf-8'))

        user = User.objects.get(pk = body["user"])
        book = Book.objects.get(pk = body["book"])
        comment = body["text"]
        stars = body["stars"]

        # search = Review.objects.get(book = book.id, user = user.id)

        # if search:
        #     search.comment = comment
        #     search.stars = stars
            
        #     search.save()

        #     return HttpResponse("Review atualizada com sucesso!")

        # else:
        review = Review.objects.create(
            user = user,
            book = book,
            comment = comment,
            stars = stars
        )

        review.save()

        return HttpResponse("Review cadastrada com sucesso!")
        

    def getReviews(request, id):
        book = Book.objects.get(pk = id)
        reviews = list((Review.objects.filter(book = book)).values())

        for item in reviews:
            print(item)
            user = list((User.objects.filter(pk = item["user_id"])).values())
            item.update(user = {"username": user[0]["username"], "id": user[0]["id"]})

        return JsonResponse(reviews, safe=False) 

        # colocar nome do user no json (esta indo so o id)