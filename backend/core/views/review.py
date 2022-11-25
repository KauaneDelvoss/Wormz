from rest_framework.viewsets import ModelViewSet
from django.http.response import HttpResponse

from core.models.review import Review, User, Book
from core.serializers import ReviewSerializer

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

        review = Review.objects.create(
            user = user,
            book = book,
            comment = comment,
            stars = stars
        )

        review.save()

        return HttpResponse("Review cadastrada com sucesso!")