from django.urls import path

from .views import RentalListView, RentalCreateView

urlpatterns = [
    path('', RentalListView.as_view(), name='rental-list'),
    path('create/', RentalCreateView.as_view(), name='rental-create'),
]
