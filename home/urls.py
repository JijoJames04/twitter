from django.urls import path

from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('summary/', views.summary, name='summary'),
    path('create-post/', views.create_post, name='create_post'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('verify_face/', views.verify_face, name='verify_face'),
]
