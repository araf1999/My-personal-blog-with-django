from django.urls import path
from . import views

urlpatterns = [
    path('members/registration.html',views.UserRegisterView.as_view(),name='register')
    
]


