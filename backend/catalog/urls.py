from django.conf import settings
from django.conf.urls.static import static
from media.router import router as media_router


from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.views import UserViewSet, BookViewSet, BookshelfViewSet, GenreViewSet

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"books", BookViewSet)
router.register(r"bookshelf", BookshelfViewSet)
router.register(r"genre", GenreViewSet)
#router.register(r"own", OwnViewSet)
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

    path('bookshelf/create', BookshelfViewSet.createBookshelf, name="createBookshelf"),
    path('bookshelf/get', BookshelfViewSet.getBookshelf, name="getBookshelf"),
    #path('update/bookshelf', BookshelfViewSet.updateBookshelf, name="updateBookshelf"),
    #path('delete/bookshelf', BookshelfViewSet.deleteBookshelf, name="deleteBookshelf"),

    # OpenAPI 3
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),

  
    ]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
