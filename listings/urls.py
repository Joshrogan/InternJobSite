from django.urls import path
from . import views

urlpatterns = [
        path('', views.ListingListView.as_view(), name='listing_list'),
        path('<int:pk>/', views.ListingDetailView.as_view(), name='listing_detail'),
]
