from django.db import models
from django.core.validators import MinValueValidator


class Salon(models.Model):
    title = models.CharField('название', max_length=100)
    address = models.CharField('адрес', max_length=100)

    class Meta:
        verbose_name = 'Салон'
        verbose_name_plural = 'Салоны'

    def __str__(self):
        return f"{self.title} - {self.address}"


class ServiceCategory(models.Model):
    title = models.CharField('Категория услуг',max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField('Наименование услуги',max_length=100)
    price = models.DecimalField(verbose_name='Цена',
                                max_digits=10,
                                decimal_places=3,
                                validators=[MinValueValidator(0)])
    category = models.ForeignKey(ServiceCategory,
                                 on_delete=models.CASCADE,
                                 related_name='services',
                                 verbose_name='Категория')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.title


class Employee(models.Model):
    first_name = models.CharField('Имя', max_length = 100)
    last_name = models.CharField('Фамилия', max_length = 100)
    date_of_birth = models.DateField('Дата рождения', db_index=True, null=True, blank=True)
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, related_name='employees',verbose_name='Салон')
    avatar = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True)
    service_category = models.ForeignKey(ServiceCategory,
                                         on_delete=models.CASCADE,
                                         related_name='employees',
                                         verbose_name='Категория услуг')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Client(models.Model):
    first_name = models.CharField('Имя', max_length = 100)
    last_name = models.CharField('Фамилия', max_length = 100)
    date_of_birth = models.DateField('Дата рождения', db_index=True, null=True, blank=True)
    phone_number = models.CharField('Телефонный номер', max_length=15)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Appointment(models.Model):
    date_time = models.DateField(null=True,verbose_name='Дата посещения')
    visit_time = models.TimeField(db_index=True, verbose_name='время посещения')
    client = models.ForeignKey(Client,on_delete=models.CASCADE, related_name='appointments',verbose_name='клиент')
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='appointments')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='appointments',verbose_name='услуга')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return f"{self.visit_time} - {self.client}"


class Shedule(models.Model):
    start_time = models.TimeField(verbose_name='Начало приема')
    end_time = models.TimeField(verbose_name='Конец приема')

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"





# Create your models here.
