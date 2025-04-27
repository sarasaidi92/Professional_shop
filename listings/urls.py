from django.urls import path
from  .views import listings, listing_detail

urlpatterns = [
    path('', listings, name='listings'),
    path('detail/', listing_detail, name='listing_detail'),

]
