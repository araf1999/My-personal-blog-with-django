from django.db import models
from blog.views import post
from django.contrib import admin
from django.db.models.expressions import F
from .models import post,Author,Tag,Comment

# Register your models here.
class postAdmin(admin.ModelAdmin):
    list_filter = ("author","date","tag")
    list_display =("title","date","author")
    prepopulated_fields={"slug":("title",)}


admin.site.register(post,postAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment)