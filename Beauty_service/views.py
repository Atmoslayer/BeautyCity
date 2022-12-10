from django.shortcuts import render, HttpResponse
from .models import Salon, ServiceCategory, Service,  Employee,Shedule
from datetime import datetime, date, time,timedelta


def index(request):
    return render(request, 'index.html', context={})


# def service(request):
#     salon = Salon.objects.all()
#     service_category = ServiceCategory.objects.all()
#     employers = Employee.objects.all()
#     context = {
#                'salons': salon,
#                'service_category': service_category,
#                'employers': employers,
#               }
#     return render(request, 'service.html', context=context)

def service(request):
    salon = Salon.objects.all()
    service_category = ServiceCategory.objects.all()
    employers = Employee.objects.all()
    shedule = Shedule.objects.get(id=1)
    shedule_start_time = shedule.start_time
    shedule_end_time = shedule.end_time
    delta_hour = datetime.combine(date.today(), shedule_end_time)-datetime.combine(date.today(),shedule_start_time)
    working_hour = [str(time(shedule_start_time.hour + i,shedule_start_time.minute)) for i in range(delta_hour.seconds//3600)]
    context = {'salons': salon,
               'service_category': service_category,
               'hours': working_hour,
               'employers': employers,
    }
    return render(request, 'service.html', context=context)


def account(request):
    return render(request, 'notes.html', context={})


def appointment(request):
    print(request.POST, request.FILES)
    return HttpResponse("OK")
