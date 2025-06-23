from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Vista para la página de inicio pública
def home_view(request):
    return render(request, 'home.html')

# Redirección automática según estado de autenticación
def home_redirect_view(request):
    if request.user.is_authenticated:
        return redirect('tiempo_real')
    else:
        return redirect('login')

# Vista principal de monitoreo (requiere login)
@login_required
def real_time_view(request):
    return render(request, 'clima/real_time.html')

# Registro de nuevos usuarios
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
