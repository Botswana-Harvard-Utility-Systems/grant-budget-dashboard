from django.views.generic import TemplateView
from django.apps import apps as django_apps
from edc_base.view_mixins import EdcBaseViewMixin
from edc_navbar import NavbarViewMixin


class HomeView(EdcBaseViewMixin, NavbarViewMixin, TemplateView):
    template_name = 'grant_dashboard/home.html'
    navbar_name = 'grant'
    navbar_selected_item = 'home'
