from django.views.generic import ListView, DetailView
from . import models

class ListingListView(ListView):
    model = models.Listing
    template_name = 'listing_list.html'

class ListingDetailView(DetailView):
    model = models.Listing
    template_name = 'listing_detail.html'
