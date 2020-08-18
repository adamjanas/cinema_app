from django.shortcuts import render, redirect
from app.users.forms import UserRegisterForm, UserAdminCreateForm
from app.users.decorators import superuser_required
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy


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


@superuser_required()
class CreateAdminView(CreateView):
    form_class = UserAdminCreateForm
    success_url = reverse_lazy('login')
    template_name = 'users/register.html'
