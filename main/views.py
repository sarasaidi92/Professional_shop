from django.shortcuts import render
from django.http import HttpResponse
from .models import Basic
from colleague.models import *
from listings.models import Listing
from listings.search_options import *

def index(request):
    basics = Basic.objects.all()
    listings = Listing.objects.order_by('-list_date')[:3]
    context = {
        'basics': basics,
        'listings': listings,
        'all_options': all_options
    }
    return render(request, template_name= 'index.html', context=context)

def about(request):
    colleagues = Colleague.objects.all()
    return render(request, template_name= 'about.html', context={'colleagues':colleagues})