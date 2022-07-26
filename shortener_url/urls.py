from django.urls import path

from . import views

urlpatterns = [
    path('', views.short, name='short'),
    # example: details/my_url/
    path('details/<str:alias>/', views.short_details, name='short_details'),
    # example: goto/my_url/
    path('goto/<str:alias>/', views.link_to, name='link_to'),
]
