from django.shortcuts import render
from .models import Testimonial
# Create your views here.


def homepage(request):
    return render(request, 'homepage.html')


def program(request):
    return render(request, 'program.html')


def about(request):
    return render(request, 'about.html')


def testimonials(request):
    return render(request, 'testimonials.html')


def resources(request):
    return render(request, 'resources.html')


def acknowledgement(request):
    return render(request, 'acknowledgement.html')