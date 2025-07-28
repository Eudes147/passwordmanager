from django.shortcuts import render,redirect
from .models import PasswordManager
from .forms import PasswordManagerForm

# Create your views here.
def addPassword(request):
    form = PasswordManagerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("dashboard")
    return render(request,"addPassword.html",context={"form":form})

def dashboard(request):
    passwords = PasswordManager.objects.all()
    return render(request,"dashboard.html",{'passwords':passwords})

def editPassword(request,id):
    passwordmanager=PasswordManager.objects.get(pk=id)
    form = PasswordManagerForm(request.POST or None,instance=passwordmanager)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request,"addPassword.html",context={"form":form,"password":passwordmanager})

def deletePassword(request, id):
    passwordmanager=PasswordManager.objects.get(pk=id)
    if request.method=="POST":
        passwordmanager.delete()
        return redirect("dashboard")
    
    return render(request,"confirmationdelete.html",{"passwordManager":passwordmanager})
    