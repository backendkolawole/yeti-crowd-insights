from rest_framework import serializers
from config_app.models import Feed, FeedPolygon, Event
from config_app.models import Client

class FeedPolygonSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeedPolygon
        fields = "__all__"


class FeedSerializer(serializers.ModelSerializer):

    polygons = FeedPolygonSerializer(many=True, read_only=True)

    class Meta:
        model = Feed
        # fields = "__all__"
        exclude = ['event']


class EventSerializer(serializers.ModelSerializer):

    feed = FeedSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        exclude = ['client']


class ClientSerializer(serializers.ModelSerializer):

    event = EventSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ["id", "event", "username", "email"]
