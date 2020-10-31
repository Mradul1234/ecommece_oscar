from django.db import models
from oscar.apps.catalogue.abstract_models import AbstractProduct
class Product(AbstractProduct):
    points = models.IntegerField(blank=True, null=True)

from oscar.apps.catalogue.models import *  # noqa isort:skip
