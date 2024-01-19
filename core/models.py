from django.db import models
from datetime import date
from django.utils.timezone import now
# Create your models here.


class Image (models.Model):
    name = models.CharField(max_length=100, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='images/')
    uploadDate = models.DateTimeField(default=now)

    def __str__(self):
        return self.name


class Author (models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class BlogPost (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publishDate = models.DateTimeField(default=now)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
