from .models import Detail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from datetime import datetime
from django.contrib.auth.models import User

from django.utils import timezone
import sched, time

def details_list(request):
    return render(request, 'shop/details_list.html', {})

@login_required
def home(request):
    return render(request, 'shop/details_list.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def new_detail(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            car = request.POST['car']
            author = request.user
            detail = request.POST['detail']
            type_of_detail = request.POST['type_of_detail']
            price = request.POST['price']
            description = request.POST['description']
            post = Detail(car = car, type_of_detail = type_of_detail, author = author, detail = detail, price = price, description = description)
            post.save()
            return redirect('/')
    else:
        return redirect('/login/')
    return render(request, 'shop/new_detail.html')