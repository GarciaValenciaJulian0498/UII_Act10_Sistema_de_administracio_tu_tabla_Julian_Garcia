from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Profesor  
from .forms import ProfesorForm
from django.shortcuts import get_object_or_404, redirect

def index(request):
    return render(request, 'profesor/index.html', {
        'profesor': Profesor.objects.all()
    })

def ver_profesores(request, id):
    profesor = Profesor.objects.get(pk=id)
    return render(request, 'profesor/ver_profesores.html', {'profesor': profesor})

def agregar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            nuevo_profesor_nombre = form.cleaned_data['nombre']
            nuevo_profesor_apellido_pat = form.cleaned_data['apellido_pat']
            nuevo_profesor_apellido_mat = form.cleaned_data['apellido_mat']
            nuevo_profesor_email = form.cleaned_data['email']
            nuevo_profesor_telefono = form.cleaned_data['telefono']
        
            nuevo_profesor = Profesor(
                nombre=nuevo_profesor_nombre,
                apellido_pat=nuevo_profesor_apellido_pat,
                apellido_mat=nuevo_profesor_apellido_mat,
                email=nuevo_profesor_email,
                telefono=nuevo_profesor_telefono
            )

            nuevo_profesor.save()
            return render(request, 'profesor/agregar_profesor.html', {
                'form': ProfesorForm(),
                'success': True
            })

    else:
        # ✅ Aquí cargas el formulario cuando entras a la página
        form = ProfesorForm()

    return render(request, 'profesor/agregar_profesor.html', {'form': form})
def editar_profesor(request, id):
    profesor = Profesor.objects.get(pk=id)

    if request.method == 'POST':
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('ver_profesores', id=profesor.id) 
    else:
        form = ProfesorForm(instance=profesor)

    return render(request, 'profesor/editar_profesor.html', {
        'form': form,
        'success': False
    })
def borrar_profesor(request, id):
    profesor = get_object_or_404(Profesor, id=id)
    
    if request.method == "POST":
        profesor.delete()
        return redirect('borrar_success')  # Redirige a la página de éxito
    
    # Si es GET, mostramos la confirmación
    return render(request, 'profesor/confirmar_borrar.html', {'profesor': profesor})

def borrar_success(request):
    return render(request, 'profesor/borrar_success.html')