from urllib import request
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth.models import User
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('newpost/', views.createPost, name='newpost'),
    path("post/<str:pk>/", views.getPost, name='detail' ),
    path('post/<str:pk>/delete/', views.deletePost, name='deletepost'),
    path('post/<str:pk>/edit', views.updatePost, name='update'),
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('deletecomment/', views.deleteComment, name = 'deletecomment'),
    path('user/', views.Profile, name='user' ),
    path('accountsetting/', views.accountSettings, name='account' ),
    path('userspost/', views.allPosts, name='userposts' ),
    path('featurepost/', views.featurePost, name='features' ),
    path("getfeature/<str:pk>/", views.getfeatures, name='featuredetail' ),
    path('featurepost/<str:pk>/delete/', views.deletefeaturePost, name='deletefeaturepost'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
