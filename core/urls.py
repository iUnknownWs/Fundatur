from django.urls import path, include
from rest_framework import routers
from .views import BlogPostViewSet, AuthorViewSet, ImageViewSet

router = routers.DefaultRouter()
router.register(r'blogpost', BlogPostViewSet)
router.register(r'author', AuthorViewSet)
router.register(r'image', ImageViewSet)

urlpatterns = [
    path('', include(router.urls))
]
