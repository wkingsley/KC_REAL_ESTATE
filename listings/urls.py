from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'), #will be /listings
    path('<int:listing_id>', views.listing, name='listing'), #will be /listings/id
    path('search', views.search, name='search'),
]