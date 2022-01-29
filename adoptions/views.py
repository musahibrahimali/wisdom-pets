from django.shortcuts import render
from .models import Pet
from django.http import Http404
from django.http import HttpResponse


# Home View
def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html', {
        'Pets': pets,
    })


def pet_detail(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404("Pet not found")
    return render(request, 'pet_detail.html', {
        "pet": pet,
    })
