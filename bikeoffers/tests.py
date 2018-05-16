from django.test import TestCase
from django.utils import timezone

from .models import Rental


class RentalModelTests(TestCase):

    def test_hour_rental_paid(self):
        rental = Rental(
            client='User',
            date=timezone.now(),
            rental_type=Rental.HOUR,
            rental_time=1,
            bike_qty=1
        )
        self.assertEqual(rental.paid_amount, 5)

    def test_hour_rental_paid_family_discount(self):
        rental = Rental(
            client='User',
            date=timezone.now(),
            rental_type=Rental.HOUR,
            rental_time=1,
            bike_qty=4
        )
        self.assertEqual(rental.paid_amount, 14)

    def test_day_rental_paid(self):
        rental = Rental(
            client='User',
            date=timezone.now(),
            rental_type=Rental.DAY,
            rental_time=1,
            bike_qty=1
        )
        self.assertEqual(rental.paid_amount, 20)

    def test_day_rental_paid_family_discount(self):
        rental = Rental(
            client='User',
            date=timezone.now(),
            rental_type=Rental.DAY,
            rental_time=1,
            bike_qty=4
        )
        self.assertEqual(rental.paid_amount, 56)

    def test_week_rental_paid(self):
        rental = Rental(
            client='User',
            date=timezone.now(),
            rental_type=Rental.WEEK,
            rental_time=1,
            bike_qty=1
        )
        self.assertEqual(rental.paid_amount, 60)

    def test_week_rental_paid_family_discount(self):
        rental = Rental(
            client='User',
            date=timezone.now(),
            rental_type=Rental.WEEK,
            rental_time=1,
            bike_qty=4
        )
        self.assertEqual(rental.paid_amount, 168)
