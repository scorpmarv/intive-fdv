from django.db import models


class Rental(models.Model):
    HOUR = 0
    DAY = 1
    WEEK = 2
    RENTAL_CHOICES = (
        (HOUR, 'Hour'),
        (DAY, 'Day'),
        (WEEK, 'Week'),
    )

    client = models.CharField(max_length=100, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    rental_type = models.SmallIntegerField(
        choices=RENTAL_CHOICES,
        blank=False,
        null=False
    )
    rental_time = models.PositiveSmallIntegerField(blank=False, null=False)
    bike_qty = models.PositiveSmallIntegerField(blank=False, null=False)

    @property
    def paid_amount(self):
        unit_price = 0
        if self.rental_type == self.HOUR:
            unit_price = 5
        elif self.rental_type == self.DAY:
            unit_price = 20
        elif self.rental_type == self.WEEK:
            unit_price = 60
        if 3 <= self.bike_qty <= 5:
            unit_price *= 0.7

        return unit_price * self.rental_time * self.bike_qty
