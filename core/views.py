from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializer import BlogPostSerializer, AuthorSerializer, ImageSerializer, MapMarkerSerializer, NewsletterSerializer
from .models import BlogPost, Author, Image, MapMarker, Newsletter
# Create your views here.

class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.AllowAny]

class MapMarkerViewSet(viewsets.ModelViewSet):
    queryset = MapMarker.objects.all()
    serializer_class = MapMarkerSerializer
