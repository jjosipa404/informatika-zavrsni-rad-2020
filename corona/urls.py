from . import views
from django.urls import path, include
from corona.dash_apps.finished_apps import bar
from corona.dash_apps.finished_apps import pie
from corona.dash_apps.finished_apps import line
from corona.dash_apps.finished_apps import scatter
from corona.dash_apps.finished_apps import scattergeo
from corona.dash_apps.finished_apps import scattermapbox
from corona.dash_apps.finished_apps import travel
from .views import *


urlpatterns = [
    path('', views.home, name='index'),
    path('', include('users.urls')),
    path('index/', views.index, name='index'),
    path('world', views.world, name='world'),
    path('travel', views.travel, name='travel'),
    path('countries', views.countries, name='countries'),
    # CREATE
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/comment/new/', CommentCreateView.as_view(), name='post-comment'),
    # READ
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),   
    # UPDATE
    path('posts/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),   
    path('comments/<int:pk>/update', CommentUpdateView.as_view(), name='comment-update'),
    # DELETE
    path('posts/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),   
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]