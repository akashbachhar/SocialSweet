from django import forms
from django.forms import ModelForm
from .models import User, UserProfile


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
        }



class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profileImage', 'profileAbout', 'gender', 'profileRelationship']


        widgets = {
            'profileAbout': forms.Textarea(attrs={'placeholder': 'About'}),
        }
