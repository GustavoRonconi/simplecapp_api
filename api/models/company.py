import uuid

from django.db import models

from api.constants import States


class Company(models.Model):
    class Meta:
        db_table = "company"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=50, unique=True)
    state = models.CharField(choices=States.choices, max_length=20)
    cep = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
