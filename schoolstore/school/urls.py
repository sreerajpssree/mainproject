from django.urls import path
from . import views

app_name = 'school'
urlpatterns = [
    path("", views.index, name='index'),
    path("register/", views.register, name='register'),
    path("login/", views.login, name='login'),
    path('addstudentdetail/<int:id>/', views.addstudentdetail, name='addstudentdetail'),
    path('logout', views.logout, name='logout'),
    path('success/<str:message>/', views.success, name='success'),
]
