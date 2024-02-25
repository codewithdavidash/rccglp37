
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.db.models import Q
from .models import *
from .forms import *

# Create your views here.
@login_required
def index(request):
    profile = Profile.objects.get(user=request.user)
    a_r = AreaRecord.objects.all()
    return render(
        request=request,
        template_name='app/index.html',
        context={
            'ar': a_r,
            'profile': profile,
        })


@login_required
def my_records(request):
    profile = Profile.objects.get(user=request.user)
    a_r = AreaRecord.objects.all()
    return render(
        request=request,
        template_name='app/my_records.html',
        context={
            'ar': a_r,
            'profile': profile,
        })
    
    
@login_required
def add_record(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        form = AddRecordForm(request.POST)
        if form.is_valid():
            x = form.save(commit=False)
            x.created_by = profile
            x.save()

            return redirect('index')
        
    else:
        form = AddRecordForm()
    return render(request, 'app/add.html', context={
        'form': form
    })  


@login_required
def update_record(request, pk):
    ar= AreaRecord.objects.get(pk=pk)
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        form = UpdateRecordForm(request.POST, instance=ar)
        if form.is_valid():
            x = form.save(commit=False)
            x.created_by = profile
            x.save()

            return redirect('my_records')
        
    else:
        form = UpdateRecordForm(instance=ar)
    return render(request, 'app/update.html', context={
        'form': form
    })  
    
        
@login_required
def logoutView(request):
    logout(request)
    messages.info(request, 'Your Session has Ended')
    return redirect('login')


@login_required
def delete_record(request, pk):
    ar= AreaRecord.objects.get(pk=pk)
    if request.method == 'POST':
        ar.delete()
        return redirect('my_records')
    return render(request, 'app/delete.html', context={
        'ar': ar
    })
    

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Account Was Created Successfully!')
            us_r = User.objects.get(username=form.cleaned_data['username'])
            Profile.objects.create(
                user=us_r,
                parish_name='',
                parish_location=''
                )
            return redirect('login')
        
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', context={
        'form': form
    })
    

@login_required
def search(request):
    query = request.GET.get('query', '')
    ar = AreaRecord.objects.filter(Q(parish_name__icontains=query) |Q(area_coordinator__icontains=query) | Q(area_name__icontains=query))
    
    return render(request, 'app/search.html', context={
        'query': query,
        'ar': ar,
    })
    
    
@login_required
def detail(request, pk):
    ar = get_object_or_404(AreaRecord, pk=pk)
    return render(request, 'app/detail.html', context={
        'ar': ar,
    })
    

@login_required
def settings(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'app/settings.html', context={
        'p': profile,
    })
    
    
@login_required
def editprofile(request, pk):
    p= Profile.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=p)
        if form.is_valid():
            x = form.save(commit=False)
            x.user = request.user
            x.save()

            return redirect('settings')
        
    else:
        form = ProfileForm(instance=p)
    return render(request, 'app/updateprofile.html', context={
        'form': form
    })  

