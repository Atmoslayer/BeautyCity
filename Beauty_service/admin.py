from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline
from .models import Service, ServiceCategory, Client, Employee,Appointment,Salon,Shedule


@admin.register(Shedule)
class SheduleAdmin(admin.ModelAdmin):
    pass


class AppointmentInline(TabularInline):
    model = Appointment


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    inlines = [AppointmentInline,]



@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    pass


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    pass

# Register your models here.
