from django.shortcuts import get_object_or_404, render
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import price_per_day_choices, state_choices, desk_choices


# Create your views here.
#from urls.py calling index method inside the views.py
#var = modelname.objects.all()

def index(request):
    listings = Listing.objects.all().filter(is_published=True)

    paginator= Paginator(listings, 6)
    page=request.GET.get('page')
    paged_listings= paginator.get_page(page)
 
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)
 
def listing(request, listing_id): #listing id passed through url/ listing/2
    listing = get_object_or_404(Listing, pk=listing_id) #show if listing exists, if not error 404
    
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)
 
def search(request):
    #query search list
    queryset_list=Listing.objects.order_by('-title')
    #search by keyword 
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list= queryset_list.filter(description__icontains=keywords)
   
    #search by city iexact is case insensitive
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list= queryset_list.filter(city__iexact=city)
    
    #search by state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list= queryset_list.filter(state__iexact=state)

    #search by number of desk
    if 'number_of_desk' in request.GET:
        number_of_desk = request.GET['number_of_desk']
        if number_of_desk:
            queryset_list= queryset_list.filter(number_of_desk__gte=number_of_desk)
    
    #search by price
   # if 'price_per_day_choices' in request.GET:
    
    #    price_per_day_choices = request.GET['price_per_day_choices']
     #   if price_per_day_choices:
      
      #      queryset_list= queryset_list.filter(price_per_day_choices__lte=price_per_day_choices)

    context= {
        'price_per_day_choices': price_per_day_choices, 
        'state_choices': state_choices,
        'desk_choices': desk_choices,
        'listings': queryset_list,
        'values': request.GET,
    }
    return render(request, 'listings/search.html', context)

