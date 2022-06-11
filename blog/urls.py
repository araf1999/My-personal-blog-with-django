from django.urls import path
from . import views

urlpatterns = [
    path("",views.StatingPageView.as_view(),name="first_page")
    ,path("posts",views.AllPostsView.as_view(),name="posts"),
    path("posts/<slug:slug>",views.PostDetailView.as_view(),name="post_details")
    ,path("contactMe",views.contact,name="contactMe"),
    path("about",views.about,name="about")
]
