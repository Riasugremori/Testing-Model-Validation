from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import DeliveryProof

class DeliveryProofTests(TestCase):
    def test_price_cannot_be_negative(self):

        delivery_proof = DeliveryProof(price=-10)


        with self.assertRaises(ValidationError):
            delivery_proof.full_clean()
