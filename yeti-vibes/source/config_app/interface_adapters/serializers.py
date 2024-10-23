from rest_framework import serializers
from config_app.models import Feed, FeedPolygon, Event, EventStatus, Client, ZoneCount


class FeedPolygonSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeedPolygon
        # fields = "__all__"
        exclude = ['feed']


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


class EventCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['event_name', 'description', 'end_date',
                  'is_active']  # Exclude 'client' for creation


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['event_id', 'event_name',
                  'description', 'end_date', 'is_active']
        
    def update(self, instance, validated_data):
        instance.event_name = validated_data.get(
            'event_name', instance.event_name)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.is_active = validated_data.get(
            'is_active', instance.is_active)
        instance.save()
        return instance


class FeedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feed
        fields = ['feed_id', 'feed_name', 'rtsp_link', 'is_active']


class FeedDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feed
        fields = ['feed_id', 'feed_name', 'rtsp_link', 'is_active']

    def update(self, instance, validated_data):
        instance.feed_name = validated_data.get(
            'feed_name', instance.feed_name)
        instance.rtsp_link = validated_data.get(
            'rtsp_link', instance.rtsp_link)
        instance.is_active = validated_data.get(
            'is_active', instance.is_active)
        instance.save()
        return instance


class EventStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventStatus
        # Include all relevant fields
        fields = ['event_id', 'status', "timestamp"]


class ZoneCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZoneCount
        fields = ['event', 'polygon', 'count', 'timestamp']
