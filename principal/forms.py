from django import forms
from .models import Video, Usuario

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['titulo', 'descripcion', 'url_video', 'duracion']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el título del video'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4,
                'placeholder': 'Describe brevemente el contenido del video'
            }),
            'url_video': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://www.youtube.com/watch?v=...'
            }),
            'duracion': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': '15:30',
                'pattern': '[0-9]{1,2}:[0-9]{2}'
            }),
        }

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre'
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el apellido'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ejemplo@correo.com'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '5555-5555'
            }),
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado.")
        return email