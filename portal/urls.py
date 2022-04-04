from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('autor/add/', views.autor_add, name='autor_add'),
    path('autor/delete/<int:autor_pk>', views.autor_delete, name='autor_delete'),
    path('autor/edit/<int:autor_pk>', views.autor_edit, name='autor_edit'),
    path('autor', views.autor, name='autor'),
]