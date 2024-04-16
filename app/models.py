from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='uploads')
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk': self.pk})
