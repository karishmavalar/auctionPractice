from django.conf.urls import include, url
from .views import * 


urlpatterns = [
    url(r'^index/$', AuctionList.as_view(), name='auctions_list'),
    url(r'^details/$', AuctionDetailList.as_view(), name='auctionsdetail_list'),
    
]