from django.db import models
from category.models import Category
from django.contrib.auth.models import User

class Blog(models.Model):
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)
    tanggal_diperbarui = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    detail = models.CharField(max_length=255, default='')
    description = models.CharField(max_length=255, default='')
    file = models.FileField(upload_to='files/', default='')
    
    def __str__(self):
        return str(self.author)