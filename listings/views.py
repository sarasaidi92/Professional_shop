from django.shortcuts import render, get_object_or_404
from .models import Listing
from  django.core.paginator import Paginator

def listings(request):
    products = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings.html', context=context)

def listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listing_detail.html', context=context)


def search(request):
    queryset = Listing.objects.order_by('-list_date')
    return render(request, '_partials/_middle.header.html')
