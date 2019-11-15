from django.urls import path
from . import views

urlpatterns = [
  #  path('', views.post_list, name = 'post_list'),
    path('time/', views.get_time, name = 'get_time'),
 #   path('<str:msg>/', views.post_list_test),

]


