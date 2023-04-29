from django.shortcuts import render
from .models import country
# Create your views here.

def country_chart_view(request):
    all_countries = country.objects.all()
    return render(request , 'charts/chart.html' , {'items' : all_countries})