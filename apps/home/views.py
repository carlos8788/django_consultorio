from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    context = {}
    context['user'] = request.user
    return render(request, 'pages/index.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            print(user, 'USER')
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    
    return render(request, 'pages/login.html', {'form': form})

def services_view(request):
    return render(request, 'pages/services.html')