from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('<int:id>', views.ver_profesores, name='ver_profesores'),
    path('agregar/', views.agregar_profesor, name='agregar_profesor'),
    path('editar/<int:id>/', views.editar_profesor, name='editar_profesor'),
    path('borrar/<int:id>/', views.borrar_profesor, name='borrar_profesor'),
    path('borrar/success/', views.borrar_success, name='borrar_success')
]