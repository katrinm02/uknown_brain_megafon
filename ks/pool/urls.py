from django.urls import path
from . import views

app_name = 'pool'
urlpatterns = [
#     path('', name='index'),
    path('<str:endpoint>/<int:pool>/', views.register, name='register'),
]