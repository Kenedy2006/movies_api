from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, DirectorViewSet, ActorViewSet, GenreViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'directors', DirectorViewSet)
router.register(r'actors', ActorViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
