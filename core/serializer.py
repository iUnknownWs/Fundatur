from rest_framework import serializers
from .models import BlogPost, Author, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BlogPostSerializer(serializers.ModelSerializer):
    author_details = AuthorSerializer(source='author', read_only=True)
    author = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), write_only=True)
    image_details = ImageSerializer(source='image', read_only=True)
    image = serializers.PrimaryKeyRelatedField(
        queryset=Image.objects.all(), write_only=True)

    class Meta:
        model = BlogPost
        fields = '__all__'
