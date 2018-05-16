from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import Rental


class RentalCreateView(CreateView):
    model = Rental
    template_name = 'bikeoffers/create.html'
    fields = ['client', 'rental_type', 'rental_time', 'bike_qty']
    success_url = reverse_lazy('rental-list')


class RentalListView(ListView):
    model = Rental
    context_object_name = 'rentals'
