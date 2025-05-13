from django.urls import path
from  .views import listings, listing_detail,search

urlpatterns = [
    path('', listings, name='listings'),
    path('detail/<int:listing_id>', listing_detail, name='listing_detail'),
    path('search/', search, name='search'),

]
