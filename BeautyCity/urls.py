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
    path('authorization/', views.LoginUser.as_view(), name='authorization'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('logout/', views.LogoutUser.as_view(), name='logout'),
    path('api/appointment/', views.add_appointment, name='add_appointment'),
    path('api/masters/', views.fetch_masters, name='fetch_masters')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
