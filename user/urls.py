from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('signup/', views.handleSignup, name='handleSignup'),
                  path('login/', views.handleLogin, name='handelLogin'),
                  path('logout/', views.handleLogout, name='handelLogout'),
                  path('<str:profile_page>/', views.profilePage, name='profilePage'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
