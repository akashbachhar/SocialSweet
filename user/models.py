from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    GENDER = (
        ('👱🏻 Male', '👱🏻 Male'),
        ('🙍🏻 Female', '🙍🏻 Female'),
    )

    RELATIONSHIP = (
        ('😏 Single', '😏 Single'),
        ('😍 Comitted', '😍 Comitted'),
    )

    serial = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profileImage = models.ImageField(upload_to='profileImage', default='defaultProfileImage.png')
    profileAbout = models.TextField(max_length=1000, blank=True)
    gender = models.CharField(max_length=100, choices=GENDER, blank=True)
    profileRelationship = models.CharField(max_length=100, choices=RELATIONSHIP, blank=True)

    def __str__(self):
        return self.user.username
