from django.http import (HttpResponse, HttpResponseServerError)
from django.shortcuts import render, redirect
from carDetection.carDetectionModel import find_cars
from django.http import JsonResponse
from core.models import (Image, Stats)

from core.forms import ImageForm


def index(request):
    return HttpResponse("Hello, world. You're at index.")


def home(request):
    images = Image.objects.all()
    return render(request, 'home.html', {'images': images})


def upsert(image_form):
    new_image = image_form.save(commit=False)
    try:
        old_image = Image.objects.get(description = new_image.description)
        old_image.image.delete()
        old_image.delete()
        new_image.masked = False
        new_image.save()
    except Image.DoesNotExist:
        new_image.masked = False
        new_image.save()

    return new_image


def model_form_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_object = upsert(form)
            find_cars(image_object)
            return redirect('home')
    else:
        form = ImageForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })

def api(request):
    # breakpoint()
    stat = Stats.objects.first()
    try:
        image = Image.objects.get(masked=False)
        imageMasked = Image.objects.get(masked=True)
    except Image.DoesNotExist:
        data = {
            'error' : 'Missing Image'
        }
        return HttpResponseServerError(JsonResponse(data))
        # return JsonResponse(data)


    data = {
    'availableSpots': stat.openSpots,
    'totalSpots': stat.totalSpots,
    'updatedAt': stat.updatedAt,
    'image': image.image.url,
    'imageMasked': imageMasked.image.url
    }
    return JsonResponse(data)
