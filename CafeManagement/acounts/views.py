from django.shortcuts import render, redirect, reverse
from django.views import View
from django.http import  HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm


class LoginView(View):
    template_name = "acounts/login.html"

    def get(self, request, *args, **kwargs):

        form = LoginForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        redirect_to = request.POST.get("next", "")
        form = LoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data["phone_number"]
            password = form.cleaned_data["password"]
            user = authenticate(
                request=request, username=phone_number, password=password
            )
            if user:
                login(request, user)
                if redirect_to:
                    return HttpResponseRedirect(redirect_to)
                return HttpResponseRedirect(reverse("home"))

        error_message = "Invalid phone number or password. Please try again."
        return render(
            request, self.template_name, {"form": form, "error_message": error_message}
        )


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("login"))
