from django.urls import path

from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create-post/', views.create_post, name='create_post'),
]
