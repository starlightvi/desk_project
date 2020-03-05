from django.urls import path
from . import views
#url/path/route is attached to a method 
#'' pertains to /listings

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
]
