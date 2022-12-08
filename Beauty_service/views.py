from django.shortcuts import render
from .models import Salon, ServiceCategory, Service,  Employee


def index(request):
    return render(request, 'index.html', context={})


def service(request):
    salon = Salon.objects.all()
    service_category = ServiceCategory.objects.all()
    employers = Employee.objects.all()
    context = {
               'salons': salon,
               'service_category': service_category,
               'employers': employers,
              }
    return render(request, 'service.html', context=context)
