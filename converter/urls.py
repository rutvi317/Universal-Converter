from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('testimonial',views.testimonial,name='testimonial'),
    path('work',views.work,name='work'),
    path('contact',views.contact,name='contact'),
    path('currency', views.currency,name='currency'),
    path('unit', views.unit,name='unit'),
    path('temperature', views.temperature,name='temperature'),
    path('graph', views.graph,name='graph'),
    path('crypto', views.crypto,name='crypto'),
    
]