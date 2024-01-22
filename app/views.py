from collections import UserDict, UserList, UserString
from django.forms import PasswordInput
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import UserInfo


# Create your views here.


def home(request):
    return render(request, 'app/index.html')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username):
            messages.error(request, "Le nom d'utilisateur est pris")
            return redirect('register')
        mon_utilisateur = User.objects.create_user(username, email, password)
        mon_utilisateur.first_name =firstname
        mon_utilisateur.save()
        messages.success(request, 'Votre compte a ete cree avec success ')
        return redirect('login')
    
    return render(request, 'app/register.html')
def logISn(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                firstname = user.first_name 
                return render(request, 'app/acc.html', {'firstname': firstname})
            else:
                 messages.error(request, 'Mauvaise autnentification')
                 return redirect('login')
        return render(request, 'app/login.html')   
def logOut(request):
    logout(request,)
    messages.success(request, 'Vous avez ete deconnecter')
    return redirect('home')


def acc(request):
    if request.method == "POST":
        ip = request.POST.get('ip')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        poste = request.POST.get('poste')
        cc = request.POST.get('cc')
       

        # Crée une nouvelle instance du modèle UserInfo et sauvegarde les données dans la base de données
        user_info = UserInfo.objects.create(ip=ip, nom=nom, prenom=prenom, poste=poste, cc=cc)
        user_info.save()
        
        return render(request, 'app/valider.html')  # Rediriger vers une page de confirmation

    return render(request, 'app/votre_template.html')  # Renvoyer à une page d'inscription si ce n'est pas une requête POST

    
def valider(request):
    return render(request, 'app/valider.html')


    
