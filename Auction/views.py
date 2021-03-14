from __future__ import unicode_literals
from Auction.models import Auctions
from Auction.serializers import AuctionSerializer,AuctionDetailSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class AuctionList(APIView):
    """
    List all Auction.
    """
    def get(self, request, format=None):
        obj = Auction.objects.filter(enable=True)
        serializer = AuctionSerializer(obj, many=True)
        return Response(serializer.data)

class AuctionDetailList(APIView):
    """
    DetailList all Auction.
    """
    def get(self, request, format=None):
        obj = Auction.objects.all()
        serializer = AuctionDetailSerializer(obj, many=True)
        return Response(serializer.data)