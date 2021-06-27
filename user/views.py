from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from sweet.models import Post
from .models import UserProfile
from .forms import UserProfileForm, UserUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def profilePage(request, profile_page):
    users = User.objects.all()
    userPage = User.objects.filter(username=profile_page).first()
    userProfile = UserProfile.objects.filter(user=userPage).first()
    if request.user.is_authenticated:
        userUpdateForm = UserUpdateForm(instance=request.user)
        userProfileForm = UserProfileForm(instance=request.user.userprofile)
    else:
        userUpdateForm = UserUpdateForm()
        userProfileForm = UserProfileForm()

    posts = Post.objects.filter(user=userPage).order_by('-time')

    if request.method == 'POST':
        userUpdateForm = UserUpdateForm(request.POST, instance=request.user)
        userProfileForm = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if userUpdateForm.is_valid() and userProfileForm.is_valid():
            userUpdateForm.save(commit=True)
            userProfileForm.save(commit=True)
        return redirect(f'/user/{request.user}')

    else:
        return render(request, 'user/profile.html', {'userPage': userPage,
                                                     'users': users,
                                                     'posts': posts,
                                                     'userProfile': userProfile,
                                                     'userUpdateForm': userUpdateForm,
                                                     'userProfileForm': userProfileForm
                                                     })


def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            messages.success(request, "User Created !")
            return redirect('sweet')
        else:
            messages.error(request, "Passwords do not match ! ")
            return redirect('sweet')

    else:
        return HttpResponse("404 Error!")


def handleLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('sweet')
        else:
            messages.error(request, "User Does Not Exist ! ")
            return redirect('sweet')

    else:
        return HttpResponse("Error!")


def handleLogout(request):
    logout(request)
    return redirect('sweet')
