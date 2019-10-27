from django.db import models

# Create your models here.
class PantryItem(models.Model):
    content = models.TextField()
    image = models

class Snippet(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    font_size = models.IntegerField()

    def __str__(self):
        return self.title

    def body_preview(self):
        return self.body[:50]
