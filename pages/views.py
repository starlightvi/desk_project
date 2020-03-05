from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_per_day_choices, state_choices, desk_choices
# Create your views here.
#create methods and link those views to methods
def index (request):
    listings= Listing.objects.filter(is_published=True) [:3]

    context = {
        'listings': listings,
        'price_per_day_choices': price_per_day_choices, 
        'state_choices': state_choices,
        'desk_choices': desk_choices,
    }

    return render(request,'pages/index.html', context) #render a template for the pages (request, location of template)
 
def about (request):
    #get all realtors
    realtors= Realtor.objects.order_by('-hire_date')

    #get all MVP
    mvp_realtors= Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    

    return render(request,'pages/about.html', context)
