from django.urls import path

from . import views
from .views import AlumnoView
from .views import EliminarAlumnoView



app_name = 'web'

urlpatterns = [
    path('', views.AlumnoView.as_view(),name='index'),
    path('profesor/', views.ProfesorView.as_view(),name='profesor'), 
    path('eliminar/<int:alumno_id>/', views.EliminarAlumnoView.as_view(), name='eliminar'),
    path('eliminarp/<int:profesor_id>/', views.EliminarProfesorView.as_view(), name='eliminarp')
    
   
    

]