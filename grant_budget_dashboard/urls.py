from django.contrib import admin
from django.urls import path
from edc_dashboard import UrlConfig
from .views.home_view import HomeView

app_name = 'grant_budget_dashboard'

# budgets_listboard_url_config = UrlConfig(
#     url_name='budgets_listboard_url',
#     # view_class=ListboardView,
#     label='budgets_listboard',
#     identifier_label='subject_identifier',
#     identifier_pattern=None)
#
# urlpatterns = []
#
# urlpatterns += budgets_listboard_url_config.listboard_urls


urlpatterns = [
    path('', HomeView.as_view(), name='home')
]
