
# Create your models here.
from django.db import models


# Create your models here.
class NewsCategory(models.Model):
        category_name = models.CharField(max_length=32)
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return str(self.category_name)

class News(models.Model):
    news = models.CharField(max_length=200)
    content = models.TextField()
    photo = models.FileField(upload_to='videos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.news