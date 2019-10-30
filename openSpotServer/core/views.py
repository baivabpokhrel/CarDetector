from django.http import HttpResponse
from django.shortcuts import render, redirect
from carDetection.carDetectionModel import find_cars

from core.models import Image

from core.forms import ImageForm


def index(request):
    return HttpResponse("Hello, world. You're at index.")


def home(request):
    images = Image.objects.all()
    return render(request, 'home.html', {'images': images})


def custom_save(image_form):
    image = image_form.save(commit=False)
    image.save()
    return image


def model_form_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_object = custom_save(form)
            find_cars(image_object.image.path)
            return redirect('home')
    else:
        form = ImageForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })
