from rest_framework import serializers
from Auction.models import Auctions


class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auctions
        fields = ['name','starts_on','ends_on','featured_image','enable']
        
        
    
class AuctionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auctions
        fields = '__all__'
        
        
