from django.shortcuts import render
from .models import Salon, ServiceCategory,Service


def index(request):
    return render(request, 'index.html', context={})


def service(request):
    salon = Salon.objects.all()
    service_category = ServiceCategory.objects.all()
    context = {'salons': salon,
               'service_category':service_category,
    }
    return render(request, 'service.html', context=context)


