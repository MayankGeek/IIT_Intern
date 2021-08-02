from django.contrib import admin
from django.urls import path
from .import views
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('login/',auth_view.LoginView.as_view(template_name="index/login.html"),name="login"),
    path('logout/',auth_view.LogoutView.as_view(template_name="index/login.html"),name="logout"),
    path('upload/', views.image_upload_view,name="image_upload_view"),
    
]

