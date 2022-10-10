from django.urls import path
from . import views

app_name = "page"

urlpatterns = [
    path('', views.index, name="index"),
    path('read/', views.read, name="read"),
    path('create/', views.create, name="create"),
    path('<int:id>/', views.detail, name="detail"),
]