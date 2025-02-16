from django.db import models

# Create your models here.
class BlogModel(models.Model):
    title = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey("auth.user", on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.title