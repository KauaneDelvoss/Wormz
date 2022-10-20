from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.views import UserViewSet, BookViewSet, BookshelfViewSet, GenreViewSet, OwnViewSet, TypeViewSet, WritesViewSet


router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"books", BookViewSet)
router.register(r"bookshelf", BookshelfViewSet)
router.register(r"genre", GenreViewSet)
router.register(r"own", OwnViewSet)
router.register(r"type", TypeViewSet)
router.register(r"writes", WritesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('cadastro/', UserViewSet.cadastro, name="cadastro"),
    #path('get/user', getUser, name="getUser"),
    #path('update/user', updateUser, name="updateUser"),
    #path('delete/user', deleteUser, name="deleteUser"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]
