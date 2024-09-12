from django.contrib.auth.models import User
# from config_app.serializers import 
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Feed, FeedPolygon, Event, Client
from .serializers import FeedSerializer, FeedPolygonSerializer, EventSerializer, ClientSerializer


class FeedList(generics.ListCreateAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    # permission_classes = [IsAdminUser]
    
    
class FeedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    # permission_classes = [IsAdminUser]
    
    
class FeedPolygonList(generics.ListCreateAPIView):
    queryset = FeedPolygon.objects.all()
    serializer_class = FeedPolygonSerializer
    # permission_classes = [IsAdminUser]
    

class FeedPolygonDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = FeedPolygon.objects.all()
    serializer_class = FeedPolygonSerializer
    # permission_classes = [IsAdminUser]
    

class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # permission_classes = [IsAdminUser]


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # permission_classes = [IsAdminUser]
    

class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    # permission_classes = [IsAdminUser]


class ClientDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    # permission_classes = [IsAdminUser]



