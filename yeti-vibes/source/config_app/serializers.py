from rest_framework import serializers
from .models import Feed, FeedPolygon, Event, Client


class FeedPolygonSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedPolygon
        fields = "__all__"
        

class FeedSerializer(serializers.ModelSerializer):
    
    polygons = FeedPolygonSerializer(many=True, read_only=True)
    
    class Meta:
        model = Feed
        fields = "__all__"
        

class EventSerializer(serializers.ModelSerializer):
    
    feed = FeedSerializer(many=True, read_only=True)
    
    class Meta:
        model = Event
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    
    event = EventSerializer(many = True, read_only=True)
    
    class Meta:
        model = Client
        fields = "__all__"
