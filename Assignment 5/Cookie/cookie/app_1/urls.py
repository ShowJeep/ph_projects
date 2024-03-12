from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home),
    path('get/', views.get_cookie),
    path('del/', views.del_cookie)
]
