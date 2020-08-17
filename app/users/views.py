from django.shortcuts import render, redirect
from app.users.forms import UserRegisterForm, UserAdminCreateForm
from django.contrib import messages


def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account has been created succesfully')
            return redirect('login')
    else:
        form = UserRegisterForm
    return render(request, 'users/register.html', {'form': form})


def create_admin(request):

    if request.method == 'POST':
        form = UserAdminCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Admin Account has been created succesfully')
            return redirect('login')
    else:
        form = UserAdminCreateForm
    return render(request, 'users/register.html', {'form': form})
