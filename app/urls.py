from django.contrib import admin
from django.urls import path
from website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path('posts/', views.posts_list, name='posts'),
    path('posts/<slug:slug>/', views.post_detail, name='post_detail'),
]
