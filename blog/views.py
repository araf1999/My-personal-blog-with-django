from django.db.models.base import Model
from django.http import request
from django.shortcuts import render,get_object_or_404
#from datetime import date, time
from .models import post
from django.views.generic import ListView,DetailView
from .forms import commentForm
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from .serializers import postSerializers
from rest_framework import generics



class StatingPageView(ListView):
    template_name = "blog/index.html"
    model = post
    serializers_class = postSerializers
    ordering = ["date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data
    


class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = post
    serializers_class = postSerializers
    ordering = ["date"]
    context_object_name = "all_posts"

class PostDetailView(DetailView):
    template_name = "blog/post-detail.html"
    model = post
    def get(self,request,slug):
        onepost = post.objects.get(slug=slug)
        context = {
            "post":onepost,
            #"post_tags":post.tag.all(),
            "comment_form":commentForm()
        }
        return render(request,"blog/post-detail.html",context
    )
    def post(self,request,slug):
        comment_form = commentForm(request.POST)
        postt = post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = postt
            comment.save()
            return HttpResponseRedirect(reverse("post_details",args=[slug]))
        
        context = {
            "post":postt,
            "post_tags":post.tags.all(),
            "comment_form":commentForm()
        }
        return render(request,"blog/post-detail.html",context)



    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tag.all()
        context["comment_form"] = commentForm()
        return context

def contact(request):
    return render(request,"blog/contactMe.html")


def about(request):
    return render(request,"blog/About.html",)


 



