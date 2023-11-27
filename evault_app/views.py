from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth

# Create your views here.
def home(request):
    return render(request,'Home.html')



def SignUp(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        #password1= request.POST.get('password1')
        #password2 = request.POST['password2']
        
        data = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username)
        
        data.save()
        return redirect('login')
    return render(request,'signup.html')
def Login(request):
    if request.method=='POST':
        username = request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request.user)
            return redirect('upload')
        
    return render(request,'login.html')
def Upload(request):
    return render(request,"upload.html")

def Search(request):
    return render(request,"search.html")