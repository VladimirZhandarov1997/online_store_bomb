from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'products/test.html', {'products': 'Test Template'})


