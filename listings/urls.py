from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'), #will be /listings since it has been declared in the main url.py urlpatterns.
    path('<int:listing_id>', views.listing, name='listing'), #will be /listings/id
    path('search', views.search, name='search'),
]