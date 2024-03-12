from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="signup"),
    path('login/', views.UserLoginView.as_view(), name="login"),
    path('profile/', views.profile, name="profile"),
    path('logout/', views.logout_view, name="logout"),
    path('profile/edit_profile/', views.edit_profile, name="edit_profile"),
]