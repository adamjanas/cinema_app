from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from app.users.decorators import superuser_required
from app.users.forms import UserAdminCreateForm, UserRegisterForm


def register(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"{username} account has been created succesfully")
            return redirect("login")
    else:
        form = UserRegisterForm
    return render(request, "users/register.html", {"form": form})


@superuser_required()
class CreateAdminView(CreateView):
    form_class = UserAdminCreateForm
    success_url = reverse_lazy("login")
    template_name = "users/register.html"
