from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages


# Create your views here
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('users:home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('users:login')

    context = {'form': form}
    return render(request, "users/register.html", context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('users:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('users:home')
            else:
                messages.info(request, 'Username or Password is incorrect')

        context = {}
        return render(request, 'users/login.html', context)


def logoutUser(request):
    logout(request)
    messages.info(request, 'Successfully Logged out')
    return redirect("users:login")


def homePage(request):
    return render(request, 'users/home.html')
