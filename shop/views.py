from .models import Detail, DetailImage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, DetailForm, ImageForm
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory

from django.utils import timezone
import sched, time

def details_list(request):
    return render(request, 'shop/cars_list.html', {})


@login_required
def home(request):
    return render(request, 'shop/cars_list.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def new_detail(request):
    ImageFormSet = modelformset_factory(DetailImage,
                                        form=ImageForm, extra=10)
    if request.method == 'POST':
        form = DetailForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=DetailImage.objects.none())

        if form.is_valid() and formset.is_valid():
            detail_form = form.save()
            detail_form.save()
            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    photo = DetailImage(detail=detail_form, image=image)
                    photo.save()
            return redirect('/new_detail/')
    else:
        form = DetailForm(request.POST)
        formset = ImageFormSet(queryset=DetailImage.objects.none())
    return render(request, 'shop/new_detail.html',
    {'form': form, 'formset': formset})

def audi_a8_d2_3_3(request):
    page = request.GET.get('page', 1)
    paginator = Paginator(Detail.objects.filter(car="Audi A8 D2 3.3 TDI")[::-1], 20)
    images = DetailImage.objects.all()
    try:
        details = paginator.page(page)
    except PageNotAnInteger:
        details = paginator.page(1)
    except EmptyPage:
        details = paginator.page(paginator.num_pages)
    return render(request, 'shop/list.html', {'details': details, 'images':images})

def audi_a8_d2_3_7(request):
    page = request.GET.get('page', 1)
    paginator = Paginator(Detail.objects.filter(car="Audi A8 D2 3.7")[::-1], 20)
    images = DetailImage.objects.all()
    try:
        details = paginator.page(page)
    except PageNotAnInteger:
        details = paginator.page(1)
    except EmptyPage:
        details = paginator.page(paginator.num_pages)
    return render(request, 'shop/list.html', {'details': details, 'images':images})

def audi_a8_d2_4_2(request):
    page = request.GET.get('page', 1)
    paginator = Paginator(Detail.objects.filter(car="Audi A8 D2 4.2")[::-1], 20)
    images = DetailImage.objects.all()
    try:
        details = paginator.page(page)
    except PageNotAnInteger:
        details = paginator.page(1)
    except EmptyPage:
        details = paginator.page(paginator.num_pages)
    return render(request, 'shop/list.html', {'details': details, 'images':images})

def audi_a8_d3_3_0(request):
    page = request.GET.get('page', 1)
    paginator = Paginator(Detail.objects.filter(car="Audi A8 D3 3.0 TDI")[::-1], 20)
    images = DetailImage.objects.all()
    try:
        details = paginator.page(page)
    except PageNotAnInteger:
        details = paginator.page(1)
    except EmptyPage:
        details = paginator.page(paginator.num_pages)
    return render(request, 'shop/list.html', {'details': details, 'images':images})

def audi_a8_d3_3_7(request):
    page = request.GET.get('page', 1)
    paginator = Paginator(Detail.objects.filter(car="Audi A8 D3 3.7")[::-1], 20)
    images = DetailImage.objects.all()
    try:
        details = paginator.page(page)
    except PageNotAnInteger:
        details = paginator.page(1)
    except EmptyPage:
        details = paginator.page(paginator.num_pages)
    return render(request, 'shop/list.html', {'details': details, 'images':images})

def audi_a8_d3_4_2(request):
    page = request.GET.get('page', 1)
    paginator = Paginator(Detail.objects.filter(car="Audi A8 D3 4.2")[::-1], 20)
    images = DetailImage.objects.all()
    try:
        details = paginator.page(page)
    except PageNotAnInteger:
        details = paginator.page(1)
    except EmptyPage:
        details = paginator.page(paginator.num_pages)
    return render(request, 'shop/list.html', {'details': details, 'images':images})

def mitsubishi_3_2(request):
        page = request.GET.get('page', 1)
        paginator = Paginator(Detail.objects.filter(car="Mitsubishi Pajero Wagon 3(2000-2006) 3.2 DID")[::-1], 20)
        images = DetailImage.objects.all()
        try:
            details = paginator.page(page)
        except PageNotAnInteger:
            details = paginator.page(1)
        except EmptyPage:
            details = paginator.page(paginator.num_pages)
        return render(request, 'shop/list.html', {'details': details, 'images':images})

def mitsubishi_3_5(request):
        page = request.GET.get('page', 1)
        paginator = Paginator(Detail.objects.filter(car="Mitsubishi Pajero Wagon 3(2000-2006) 3.5 GID")[::-1], 20)
        images = DetailImage.objects.all()
        try:
            details = paginator.page(page)
        except PageNotAnInteger:
            details = paginator.page(1)
        except EmptyPage:
            details = paginator.page(paginator.num_pages)
        return render(request, 'shop/list.html', {'details': details, 'images':images})

def porshe_cayenne(request):
        page = request.GET.get('page', 1)
        paginator = Paginator(Detail.objects.filter(car="Porsche Cayenne")[::-1], 20)
        images = DetailImage.objects.all()
        try:
            details = paginator.page(page)
        except PageNotAnInteger:
            details = paginator.page(1)
        except EmptyPage:
            details = paginator.page(paginator.num_pages)
        return render(request, 'shop/list.html', {'details': details, 'images':images})

def detail_page(request, pk):
    detail = get_object_or_404(Detail, pk=pk)
    images = DetailImage.objects.filter(detail=detail)
    return render(request, 'shop/detail.html', {'detail': detail, 'images':images})
