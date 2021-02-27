from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'registration'

urlpatterns = [
    # 21/02/27 login 삽입
    path('login/', auth_views.LoginView.as_view(template_name = 'registration/login.html'), name='login'),


]

