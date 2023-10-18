from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import CreateUserForm

# Create your views here.


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You are succesfully logged in!")
            return redirect('home')
        else:
            messages.success(
                request, "Something was wrong. Please try again ....")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

# def login_user(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         # User check
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, "You have been successfully logged in")
#             return redirect('home')
#         else:
#             messages.success(
#                 request, 'Something was wrong. Please try again...')
#             return redirect('login_user')
#     else:
#         return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You are logged out...')
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            # authenticate user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request, 'You have succesfully register an account.')
            return redirect('home')
    else:
        form = CreateUserForm()
        return render(request, 'register.html', {"form": form})
    return render(request, 'register.html', {"form": form})
