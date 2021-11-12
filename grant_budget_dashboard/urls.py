from django.contrib import admin
from django.urls import path
# from edc_dashboard import UrlConfig
from .views.home_view import HomeView
from .views.staffing_budget_view import StaffingBudgetView

app_name = 'grant_budget_dashboard'


# TODO : Be change
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('staffing_budget/', StaffingBudgetView.as_view(), name='staffing_budget'),
]
