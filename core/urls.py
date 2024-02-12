from django.urls import path, include
from rest_framework import routers
from .views import BlogPostViewSet, AuthorViewSet, ImageViewSet, MapMarkerViewSet, NewsletterViewSet

router = routers.DefaultRouter()
router.register(r'blogpost', BlogPostViewSet)
router.register(r'author', AuthorViewSet)
router.register(r'image', ImageViewSet)
router.register(r'mapmarker', MapMarkerViewSet)
router.register(r'newsletter', NewsletterViewSet)

urlpatterns = [
    path('', include(router.urls))
]
