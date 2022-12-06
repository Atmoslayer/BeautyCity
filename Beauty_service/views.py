from django.shortcuts import render


def index(request):
    return render(request, 'index.html', context={})


def service(request):
    return render(request, 'service.html', context={})
