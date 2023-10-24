from django.db import models

class Category(models.Model):
    nama_category = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nama_category