from django.shortcuts import render

def listings(request):
    return render(request, 'listings.html')

def listing_detail(request):
    return render(request, 'listing_detail.html')