from operator import index
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ImageForm
from django.contrib import messages
from .models import Image

def index(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, 'Image uploaded successfully.')
            form.save()
        else:
            print(form.errors)
    else:
        form = ImageForm()
    imgs = Image.objects.all()
    return render(request, 'index.html' , {'form':form,'imgs':imgs})



    
