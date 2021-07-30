from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from edc_base.utils import get_uuid
from edc_model_wrapper import ModelWrapper


# from edc_consent import ConsentModelWrapperMixin


class GrantModelWrapper(ModelWrapper):
    model = 'grant_budget.grant'

