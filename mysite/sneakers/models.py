from tabnanny import verbose
from django.db import models

# Create your models here.

class Sneakers(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    have = models.BooleanField(default=True)
    cat = models.ForeignKey("Category", on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Обувь"
        verbose_name_plural = "Обувь"
        ordering = ['time_create', "name"]
    

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"
    

