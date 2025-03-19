from django.contrib import messages
from django.contrib.auth import get_user_model, login, password_validation
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.http import Http404
from django.shortcuts import redirect, render
from django.utils.http import urlsafe_base64_decode
from .forms import CustomUserCreationForm, UserRegistrationForm

User = get_user_model()


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("registration_success")
    else:
        form = UserRegistrationForm()
    return render(request, "myapp/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()

    return render(request, "myapp/login.html", {"form": form})


def password_reset(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_user_model().objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, user.DoesNotExist):
        raise Http404("User not found")

    if default_token_generator.check_token(user, token):
        if request.method == "POST":
            form = PasswordResetForm(request.POST)
            if form.is_valid():
                new_password = form.cleaned_data["new_password"]
                password_validation.validate_password(new_password, user)
                user.set_password(new_password)
                user.save()
                return redirect("login")
        else:
            form = PasswordResetForm()
        return render(request, "password_reset.html", {"form": form})
    else:
        raise Http404("Token is invalid or expired")


def home(request):
    return render(request, "home.html")


def index(request):
    return render(request, "index.html")


def registration_success(request):
    return render(request, "myapp/registration_success.html")
