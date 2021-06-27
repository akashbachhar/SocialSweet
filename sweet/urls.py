from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.sweet, name='sweet'),
                  path('postComment', views.postComment, name='postComment'),
                  path('<int:post_id>', views.post, name='post'),
                  path('<int:post_id>/editPost', views.editPost, name='editPost'),
                  path('<int:post_id>/deletePost', views.deletePost, name='deletePost'),
                  path('deleteComment/<int:comment_id>', views.deleteComment, name='deleteComment'),
                  path('likePost/', views.likePost, name="likePost")

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
