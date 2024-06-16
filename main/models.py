from django.db import models

# Create your models here.

# Création du modéle Article
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField()

    def __str__(self):
        return self.title