from edc_dashboard import UrlConfig

from .patterns import screening_identifier, subject_identifier
from .views import HomeView
from django.urls import path

app_name = 'grant_dashboard'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
