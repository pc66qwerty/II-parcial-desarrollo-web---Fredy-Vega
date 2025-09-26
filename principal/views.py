from django.shortcuts import render, redirect
from .models import Video, Usuario
from .forms import VideoForm, UsuarioForm

def videos(request):
    videos_lista = Video.objects.all()
    return render(request, 'videos.html', {'videos': videos_lista})

def usuarios(request):
    usuarios_lista = Usuario.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios_lista})

def creditos(request):
    return render(request, 'creditos.html')

def agregar_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('videos')
    else:
        form = VideoForm()
    return render(request, 'agregar_video.html', {'form': form})

def agregar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'agregar_usuario.html', {'form': form})