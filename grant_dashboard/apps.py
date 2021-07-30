from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'grant_dashboard'
    admin_site_name = 'training_subject_admin'
