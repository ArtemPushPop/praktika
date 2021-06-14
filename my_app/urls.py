from django.urls import path

from . import views

urlpatterns = [
    path('post', views.post, name='post'),
    path('redirect', views.redirect, name='redirect'),
    path('put_random_pic', views.put_random_pic, name='put_pic'),
    path('delete_pictures', views.delete_pictures, name='delete_pic'),
    path('delete_redirect/<int:which>', views.delete_redirect, name='delete_redirect'),
    path('get_pic', views.get_pic, name='get_pic')
]
