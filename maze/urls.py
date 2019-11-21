from django.urls import path
from . import views

urlpatterns = [
    path('', views.make_character, name = 'make_character'),
    path('make/char/step/<str:step>/', views.make_character_by_step),
    path('v2/make/char/step/<str:step>/', views.make_character_by_step_ver_template),
    path('<str:user>/v2/make/char/step/<str:step>/', views.make_character_by_step_ver_template_with_user),

]


