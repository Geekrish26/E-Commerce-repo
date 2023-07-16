from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.models import auth
from django.shortcuts import redirect


# Create your views here.
def sign_up(request):
    page_name = "sign_up.html"
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return render(request, page_name, {"error": True, "error_msg": "Username already taken"})
        if User.objects.filter(email=email).exists():
            return render(request, page_name, {"error": True, "error_msg": "Email already taken"})
        user = User.objects.create_user(username=username, email=email, password=password)
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('product:shop')
        else:
            return render(request, page_name, {"error": True, "error_msg": "Some error occurred"})
    else:  # GET METHOD
        return render(request, page_name)


def sign_in(request):
    page_name = "sign_in.html"
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        next_url = request.POST.get("next_url","")
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if next_url != "":
                return redirect(next_url)
            else:
                return redirect('product:shop')
        else:
            return render(request, page_name, {"error": True, "error_msg": "You are not authorized"})
    else:
        return render(request, page_name)


@login_required(login_url='sign_in')
def sign_out(request):
    auth.logout(request)
    return redirect('user:sign_in')

