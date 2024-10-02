from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages



# Create your views here.


def login_view(request):
     
    if request.method == 'POST':
        user_name = request.POST['uname']
        paswrd = request.POST['paswrd1']
        user = auth.authenticate(username=user_name,password=paswrd)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credential')
            return redirect('login')

    else:
   
        return render(request, 'account/login.html' )


def register_view (request):
    

    if request.method == 'POST':
        user_name=request.POST['uname']
        email_name=request.POST['Email']
        paswrd=request.POST['paswrd1']
        parswrd2=request.POST['pasword2']

        if paswrd==parswrd2:
           if User.objects.filter(username=user_name).exists():
               messages.info(request,'User name alredy exist')
               return redirect('register')
           elif  User.objects.filter(email=email_name).exists():
              messages.info(request,'Email alredy exist')
              return redirect('register')
           else:
              
                 user= User.objects.create_user(username=user_name,email= email_name,password= paswrd)
                 user.save();
                 print('user create')
                 return redirect('/')
              

        else:
            messages.info(request,'Password arent matching')
            return redirect('register')


        
    else:

   
     return render(request, 'account/register.html' )



