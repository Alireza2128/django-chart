from django.urls import path
from .views import country_chart_view

urlpatterns = [
    path('' , country_chart_view , name="charts"),
]