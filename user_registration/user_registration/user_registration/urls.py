
from django.urls import path
from app_user_registration import views

urlpatterns = [
    path('',views.home,name='home'),
    path('usuarios/', views.usuarios,name="all_users")

]
