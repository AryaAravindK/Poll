from django.shortcuts import render,redirect
from django.contrib import messages 
from django.contrib.auth.models import User,auth




def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already existing try login')
                return render(request, 'register.html')
            elif User.objects.filter(email= email).exists():
                messages.info(request,'email id already existing try login')
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email, first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,'registration successful')
                auth.login(request,user)
                return redirect('/')
        else:
            messages.info(request,'password not matching')
            return render(request, 'register.html')
        
        
    else:
        return render(request, 'register.html')



def login(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=user_name, password= password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'invalid username')
        
        
    else:
        
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')