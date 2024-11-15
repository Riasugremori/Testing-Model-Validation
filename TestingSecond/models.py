from django.core.exceptions import ValidationError
from django.db import models

class DeliveryProof(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def clean(self):
        if self.price < 0:
            raise ValidationError("Price cannot be negative.")
