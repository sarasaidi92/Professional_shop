from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            fname_ = request.POST['first_name']
            lname_ = request.POST['last_name']
            email_ = request.POST['email']
            user_ = request.POST['username']
            pass_ = request.POST['password']
            pass2_ = request.POST['password2']
            if pass_ == pass2_:
                user = User.objects.create_user(
                username=user_,
                email=email_,
                password=pass_,
                first_name=fname_,
                last_name=lname_
            )
                user.save()
                return redirect('signin')
            else:
                print('passwords do not match')
                return redirect('signup')


        return render(request, 'signin_signup.html')


def signin(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            user_ = request.POST['username']
            pass_ = request.POST['password']

            user = authenticate(username=user_, pass_=pass_)

            if user is not None:
                login(request, user)
                return redirect('index')

            else:
                print('Error, User Not Found')
                return redirect('signup')

        return render(request, 'signin_signup.html')


def signout(request):
    logout(request)
    return redirect('signin')
