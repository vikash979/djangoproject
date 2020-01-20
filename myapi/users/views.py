from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
User = get_user_model()
from users.forms import CustomUserCreationForm
from django.http import HttpResponse
from users.forms import SignUpForm
from .models import blog
from users.models import blog
#from users.tokens import account_activation_token
from django import forms
def signupv(request):
    if request.method == 'POST':
        useru = authenticate(username=request.POST['username'], password='sudha007')
        print("!!!!!!!!!!!!!", useru)
        if useru:
            print("bbbbbb")
            login(request, useru)
            return redirect('/actiyy/home/')
        else:
            print("ooooo")
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            #current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            #print("@@@@@@@@@@@@@",account_activation_token.make_token(user))
            raw_password = form.cleaned_data.get('password1')
            print(":::::::::",user.username,"@@@@@@@@@@",raw_password)
            useru = authenticate(username='wertyt', password='ranjana007')

            # if user:
            #     print("bbbbbb")
            #     #login(request, user)
            # else:
            #     print("ooooo")
            #return redirect('home')

    else:
        form = SignUpForm()
    return render(request, 'signup1.html', {'form': form})


def home_view(request):
    print(request.user.username)
    return render(request, 'home2.html', {'form': 'form'})

def blogs(request):
    

    ff = blog.objects.all()
    
    return render(request, 'home3.html', {'form': ff})

def blofdetail(request,id):
    
    movie = blog.objects.get(id=id)

    return render(request, 'home4.html', {'form':movie})
