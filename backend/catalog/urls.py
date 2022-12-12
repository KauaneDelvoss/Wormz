from django.conf import settings
from django.conf.urls.static import static
from media.router import router as media_router


from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.views import UserViewSet, BookViewSet, BookshelfViewSet, GenreViewSet, ReviewViewSet, AnswerViewSet, QuestionViewSet, FormViewSet, AnswerAssociativaViewSet, ResolvesViewSet


router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"books", BookViewSet)
router.register(r"bookshelf", BookshelfViewSet)
router.register(r"genre", GenreViewSet)
router.register(r"answer", AnswerViewSet)
router.register(r"answerassociativa", AnswerAssociativaViewSet)
router.register(r"form", FormViewSet)
router.register(r"question", QuestionViewSet)
router.register(r"resolves", ResolvesViewSet)

#router.register(r"type", TypeViewSet)
#router.register(r"writes", WritesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('cadastro/', UserViewSet.cadastro, name="cadastro"),
    path('get/user', UserViewSet.getUser, name="getUser"),
    path('update/user', UserViewSet.updateUser, name="updateUser"),
    path('delete/user', UserViewSet.deleteUser, name="deleteUser"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/media/', include(media_router.urls)),

    path('quizz/create', AnswerAssociativaViewSet.createQuiz, name="createQuiz"),
    path('quizz/bookshelf', AnswerAssociativaViewSet.BookshelfQuiz, name="bookshelfQuiz"),
    path('quizz/createBookshelfQuiz', BookshelfViewSet.createBookshelfQuiz, name="createBookshelfQuiz"),

    path('bookshelf/create', BookshelfViewSet.createBookshelf, name="createBookshelf"),
    path('post/addBookshelf', BookshelfViewSet.addBookshelf, name="addBookshelf"),
    path('get/<slug:user_username>/bookshelf', BookshelfViewSet.getBookshelves, name="getBookshelves"),
    path('get/<slug:user_username>/bookshelf/<int:id>', BookshelfViewSet.getBookshelf, name="getBookshelf"),
    path('post/editBookshelf', BookshelfViewSet.editBookshelf, name="editBookshelf"),
    path('delete/bookshelf/<int:id>', BookshelfViewSet.deleteBookshelf, name="deleteBookshelf"),

    path('get/book/<int:id>', BookViewSet.getBook, name="getBook"),
    path('get/book/search/<slug:search>', BookViewSet.getSearch, name ="search"),

    path('post/review', ReviewViewSet.submitReview, name="submitReview"),
    path('get/reviews/<int:id>', ReviewViewSet.getReviews, name="getReviews")
  
    ]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
