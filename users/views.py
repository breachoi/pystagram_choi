from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from users.forms import LoginForm, SignupForm
from users.models import User

# Create your views here.
def login_view(request):

    if request.user.is_authenticated:
        return redirect("/posts/feeds/")

    if request.method == "POST":
            form = LoginForm(data=request.POST)

            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]

                user = authenticate(username=username, password=password)

                if user:
                    login(request, user)
                    return redirect("/posts/feeds/")
                else:
                    form.add_error(None, "cannot find the user")

            context = {"form": form}
            return render(request, "user/login.html", context)
    else:
        form = LoginForm()
        context = {"form": form}
        return render(request, "user/login.html", context)

def logout_view(request):
    logout(request)

    return redirect("/users/login/")

def signup(request):
    if request.method == "POST":
        form = SignupForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/posts/feeds/")

    else:
        form = SignupForm()

    context = {"form": form}
    return render(request, "user/signup.html", context)
