from rest_framework import serializers
from config_app.models import Feed, FeedPolygon, Event, EventStatus, Client, ZoneCount


class FeedPolygonSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeedPolygon
        # fields = "__all__"
        exclude = ['feeds']


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ["id", "username", "email"]

    def create(self, validated_data):
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance


class EventSerializer(serializers.ModelSerializer):

    client = ClientSerializer(read_only=True)

    class Meta:
        model = Event
        fields = "__all__"
        # exclude = ['client']


class FeedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feed
        # fields = "__all__"
        fields = ['feed_id', 'feed_name', 'rtsp_link', 'is_active']
        # exclude = ['event']


class EventStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventStatus
        fields = ['event_id', 'status', "timestamp"]  # Include all relevant fields



class ZoneCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZoneCount
        fields = ['event', 'polygon', 'count', 'timestamp']