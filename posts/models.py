from django.db import models

# Import the FroalaField
from froala_editor.fields import FroalaField


class Article(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title


class Page(models.Model):
    title = models.CharField(max_length=255)
    # Froala WYSIWYG Editor
    content = FroalaField()
    # Relate the page to an article
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.title} part of {self.article}'