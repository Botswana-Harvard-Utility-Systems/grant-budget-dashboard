from django.views.generic import TemplateView
from django.apps import apps as django_apps


class HomeView(TemplateView):
    template_name = 'grant_budget_dashboard/home.html'
