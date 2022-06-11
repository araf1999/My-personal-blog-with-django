from django import forms
from .models import Comment

class commentForm(forms.ModelForm):
    class Meta:
        db_table = ''
        model = Comment
        exclude = ["post"]
        labels = {"user_name" : "your name:",
        "user_email":"your email:",
        "text":"your comment:"
        }