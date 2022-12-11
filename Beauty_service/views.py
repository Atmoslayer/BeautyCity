from django.core import serializers
from django.shortcuts import render, HttpResponse
from .models import Salon, ServiceCategory, Service, Employee, Shedule, Appointment, Client
from datetime import datetime, date, time, timedelta
from rest_framework.decorators import api_view
from rest_framework import status

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


@api_view(['POST'])
def add_appointment(request):
    serialized_appointment = request.data
    try:
        current_client = Client.objects.all().first()
        first_name, last_name = serialized_appointment['serviceman'].split(' ')
        serviceman = Employee.objects.filter(last_name=last_name, first_name=first_name).first()
        service = Service.objects.filter(title=serialized_appointment['service_name']).first()
        new_appointment = Appointment.objects.create(
            date_time=datetime.strptime(serialized_appointment['appointment_date'], "%d.%M.%Y"),
            visit_time=serialized_appointment['appointment_time'],
            client=current_client,
            employee=serviceman,
            service=service,
        )
        return HttpResponse(f"Записали вас на "
                            f"{serialized_appointment['appointment_date']}-{serialized_appointment['appointment_time']}")
    except Exception:
        return HttpResponse('Что то пошло не так, запишитесь по телефону', status=status.HTTP_204_NO_CONTENT)



# def add_appointment(request):
#     print(request.POST, request.FILES)
#     salon = Salon.objects.filter(address=request.POST['salon']).first()
#     first_name, last_name = request.POST['serviceman'].split(' ')
#     serviceman = Employee.objects.filter(last_name=last_name, first_name=first_name).first()
#     service = Service.objects.filter(title=request.POST['service_name']).first()
#     date_time = datetime.strptime(request.POST['appointment_date'], "%d.%M.%Y")
#     visit_time = request.POST['appointment_time']
#     client = Client.objects.first()
#     Appointment.objects.create(
#                                 date_time = date_time,
#                                 employee=serviceman,
#                                 visit_time=visit_time,
#                                 service=service,
#                                 client=client,
#                                )
#     return HttpResponse("OK")


def fetch_masters(request):
    salon = Salon.objects.filter(address=request.GET['salon']).first()
    masters = Employee.objects.filter(salon=salon)
    data = serializers.serialize("json", masters)
    return HttpResponse(data)


def authorization(request):
    return render(request, 'authorization.html', context={})