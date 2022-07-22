from django.urls import path

from . import views

urlpatterns = [
    path('', views.short, name='short'),
    # example: /my_url/
    path('<str:alias>/', views.link_to, name='link_to'),
]