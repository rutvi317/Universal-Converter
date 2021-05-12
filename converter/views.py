from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def work(request):
    return render(request, "works.html")

def testimonial(request):
    return render(request, "testimonial.html")

def contact(request): 
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        message = request.POST['message']
        send_mail(
            'test',
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        print(name,email,number,message)
    return render(request, "contact.html")

def currency(request):
    return render(request, "currency.html")

def unit(request):
    return render(request, "unit.html")

def temperature(request):
    return render(request, "temperature.html")

def graph(request):
    return render(request, "graph.html")

def crypto(request):
    return render(request, "crypto.html")