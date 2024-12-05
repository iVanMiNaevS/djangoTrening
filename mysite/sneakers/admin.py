from django.contrib import admin

# Register your models here.
from .models import *

class SneakersAdmin(admin.ModelAdmin):
    list_display = ('id', "name", "time_create", 'photo', "have")
    list_display_links = ('id', "name")
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', "name")
    list_display_links = ('id', "name")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Sneakers, SneakersAdmin)
admin.site.register(Category, CategoryAdmin)