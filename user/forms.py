from django.forms import ModelForm
from .models import User, UserProfile


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profileImage', 'profileAbout', 'gender', 'profileRelationship']
