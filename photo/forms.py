from django.forms import ModelForm, fields
from .models import PhotoPost

class PhotoPostForm(ModelForm):
    class Meta:
        model = PhotoPost
        fields = ['category','title','comment','image1','image2']