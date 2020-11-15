from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth import login as login_, authenticate, logout as logout_
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import LoginForm, RegisterForm


@login_required
def index(request):
    return HttpResponse(
        "This is the homepage.<br> <a href='{}'>注销</a>".format(reverse("logout")))


def login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get("username"),
                password=form.cleaned_data.get("password")
            )
            if user is not None:
                login_(request, user)
                next_ = request.GET.get("next") or reverse("index")
                return redirect(next_)
            form.add_error("username", "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login_(request)
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


def logout(request):
    if request.user.is_authenticated:
        logout_(request)
    return redirect(reverse("login"))
