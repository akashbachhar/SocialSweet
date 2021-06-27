from django import forms
from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']

        widgets = {
            'content': forms.Textarea(attrs= {'class': 'createPostCaption', 'placeholder': 'Post a Sweet !'})
        }
