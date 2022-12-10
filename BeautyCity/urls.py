from django.contrib import admin
from django.urls import path
from Beauty_service import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('account/', views.account, name='notes'),
    path('api/appointment/', views.add_appointment, name='add_appointment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
