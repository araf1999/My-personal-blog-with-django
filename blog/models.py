from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    def fulName(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.fulName()


class post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    desc = models.TextField()
    image = models.ImageField(upload_to="posts",null=True)
    slug = models.SlugField(unique=True,db_index=True)
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,null=True,related_name="posts")
    tag = models.ManyToManyField(Tag,related_name="post_tags")

class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=200)
    post = models.ForeignKey(post,on_delete=CASCADE,related_name="comments")


    def __str__(self):
        return self.user_name


    

   


    


    