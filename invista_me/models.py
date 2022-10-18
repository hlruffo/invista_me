from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime


class Investimentos(models.Model):
    investimento = models.TextField(max_length=255)
    valor = models.FloatField()
    pago = models.BooleanField(default=False)
    data = models.DateField(default=datetime.now)
