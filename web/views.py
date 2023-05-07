from django.shortcuts import render, redirect


# importamos la clase View
from django.views import View
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404, redirect, render
# Create your views here.
class AlumnoView(View):
    


    def get(self,request):
        listaAlumnos = TblAlumno.objects.all()
        formAlumno = AlumnoForm()
        context = {
            'alumnos' : listaAlumnos,
            'formAlumno' : formAlumno
            
        }
        return render(request,'index.html',context)
    

    def post(self, request):
        formAlumno = AlumnoForm(request.POST)
        if formAlumno.is_valid():
            formAlumno.save()
            return redirect('/')
        
class EliminarAlumnoView(View):
    
    def post(self, request, alumno_id):
        alumno = get_object_or_404(TblAlumno, pk=alumno_id)
        alumno.delete()
        return redirect('web:index')
    
class ProfesorView(View):
    


    def get(self,request):
        listaProfesores = TblProfesor.objects.all()
        formProfesor = ProfesorForm()
        context = {
            'profesores' : listaProfesores,
            'formProfesor' : formProfesor
            
        }
        return render(request,'profesor.html',context)
    

    def post(self, request):
        formProfesor = ProfesorForm(request.POST)
        if formProfesor.is_valid():
            formProfesor.save()
            return redirect('web:profesor')

class EliminarProfesorView(View):
    
    def post(self, request, profesor_id):
        profesor = get_object_or_404(TblProfesor, pk=profesor_id)
        profesor.delete()
        return redirect('web:profesor') 