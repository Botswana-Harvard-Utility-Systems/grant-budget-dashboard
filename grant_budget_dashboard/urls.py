"""grant_budget_dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from edc_dashboard import UrlConfig

app_name = 'grant_budget_dashboard'

budgets_listboard_url_config = UrlConfig(
    url_name='budgets_listboard_url',
    # view_class=ListboardView,
    label='budgets_listboard',
    identifier_label='subject_identifier',
    identifier_pattern=None)

urlpatterns = []

urlpatterns += budgets_listboard_url_config.listboard_urls
