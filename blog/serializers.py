from django.db.models import fields
from rest_framework import serializers
from .models import post


class postSerializers(serializers.ModelSerializer):
    class Meta:

        model = post
        fields = ['id','title','excerpt','date','desc','image','slug','author','tag']

