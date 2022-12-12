from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.core import serializers
from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from .models import Salon, ServiceCategory, Service, Employee, Shedule, Appointment, Client
from datetime import datetime, date, time, timedelta
from rest_framework.decorators import api_view
from rest_framework import status
from .forms import AuthUserForm, RegisterUserForm
import uuid
from yookassa import Configuration, Payment
from django.shortcuts import redirect
from django.conf import settings




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
    current_client = Client.objects.filter(user_id=request.user.id).first()

    upcoming_appointments = []
    past_appointments = []
    price = 0
    client_appointments = current_client.appointments.all()

    for client_appointment in client_appointments:
        employee = client_appointment.employee
        service = client_appointment.service
        service_category = employee.service_category
        salon = employee.salon

        time_now = datetime.now()
        appointment_date_time = client_appointment.date_time
        appointment_visit_time = client_appointment.visit_time
        visit_time = datetime.combine(appointment_date_time, appointment_visit_time)

        price += service.price

        appointment_data = {
            'id': client_appointment.id,
            'date_time': appointment_date_time,
            'visit_time': appointment_visit_time,
            'employee_first_name':  employee.first_name,
            'employee_last_name': employee.last_name,
            'category': service_category.title,
            'address': salon.address,
            'service_type': service.title,
            'price': service.price
        }

        if time_now >= visit_time:
            past_appointments.append(appointment_data)
        else:
            upcoming_appointments.append(appointment_data)



    client_data = {
        "first_name": current_client.first_name,
        "last_name": current_client.last_name,
        "date_of_birth": current_client.date_of_birth,
        "phone_number": current_client.phone_number,
        "past_appointments":  past_appointments,
        "upcoming_appointments": upcoming_appointments,
        "price": price
    }

    print(client_data["price"])

    return render(request, 'notes.html', context=client_data)


def service_finally(request):
    return render(request, 'serviceFinally.html', context={})


@api_view(['POST'])
def add_appointment(request):
    serialized_appointment = request.data
    try:

        current_client = Client.objects.filter(user_id=request.user.id).first()
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
        #print(new_appointment.__dict__)
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


def register(request):
    return render(request, 'register.html', context={})


def update_profile(request):
    print(request.POST)
    return HttpResponseRedirect("/account/")


class RegisterUser(CreateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('notes')
    success_msg = 'Пользователь создан'

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username, password=password)
        print(aut_user.__dict__)
        login(self.request, aut_user)
        new_client = Client.objects.get_or_create(
            user_id=aut_user.id,
            first_name=aut_user.first_name,
            last_name=aut_user.last_name,
            phone_number=form.cleaned_data['phone_number']
        )
        print(new_client)
        return form_valid


class LoginUser(LoginView):
    form_class = AuthUserForm
    template_name = 'authorization.html'

    success_url = reverse_lazy('notes')

    def get_success_url(self):
        return self.success_url


class LogoutUser(LogoutView):
    next_page = reverse_lazy('authorization')


@api_view(['GET', 'POST'])
def create_payment(request):
    Configuration.account_id = settings.PAYMENT_ID
    Configuration.secret_key = settings.PAYMENT_KEY
    appointment = Appointment.objects.filter(client__user_id=request.user.id).first()
    domain = "http://127.0.0.1:8000"
    payment = Payment.create({
        "amount": {
            "value": appointment.service.price,
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": domain
        },
        "capture": True,
        "description": f"Услуга - {appointment.service};  Клиент - {appointment.client}"

    }, uuid.uuid4())
    return redirect(payment.confirmation.confirmation_url)
