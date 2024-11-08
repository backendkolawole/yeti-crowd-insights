# config_app/repositories/Feed_repository.py
from config_app.models import Feed as FeedModel, Event
from rest_framework.exceptions import NotFound
from config_app.models import Feed as FeedModel, FeedStatus as FeedStatusModel
from rest_framework.exceptions import NotFound
from datetime import datetime
from yolov8_region_counter import run, stop_the_feed
import threading
from yolov8_region_counter import stop_feed


class FeedRepository:
    def create_feed(self, client, event_id, data):
        try:
            feed_event = Event.objects.get(client=client, event_id=event_id)
        except Event.DoesNotExist:
            raise NotFound("No Event Found")

        feed = FeedModel(event=feed_event, **data)
        feed.save()
        return feed

    def get_all_feed(self, client, event_id):
        try:
            feed_event = Event.objects.get(
                client=client, event_id=event_id)
        except Event.DoesNotExist:
            raise NotFound("No Event Found")

        feeds = FeedModel.objects.filter(event=feed_event)

        return feeds

    def get_feed(self, client, event_id, feed_id):
        try:
            feed_event = Event.objects.get(client=client, event_id=event_id)
        except Event.DoesNotExist:
            raise NotFound("No Event Found")

        try:
            feed = FeedModel.objects.get(event=feed_event, feed_id=feed_id)
        except FeedModel.DoesNotExist:
            raise NotFound("No feed found")
        return feed

    def update_feed(self, client, event_id, feed_id, data):
        try:
            feed_event = Event.objects.get(client=client, event_id=event_id)
        except Event.DoesNotExist:
            raise NotFound("No Event Found")

        try:
            feed = FeedModel.objects.get(event=feed_event, feed_id=feed_id)
        except FeedModel.DoesNotExist:
            raise NotFound("No feed found")

        for key, value in data.items():
            setattr(feed, key, value)
        feed.save()

        return feed

    def delete_feed(self, client, event_id, feed_id):
        feed_event = Event.objects.get(client=client, event_id=event_id)

        feed = FeedModel.objects.get(event=feed_event, feed_id=feed_id)
        feed.delete()
        return {"success"}

    def start_the_feed(self, client, event_id, feed_id):
        try:
            event = Event.objects.get(client=client, event_id=event_id)
        except Event.DoesNotExist:
            raise NotFound("No Event Found")

        try:
            feed = FeedModel.objects.get(event=event, feed_id=feed_id)
        except FeedModel.DoesNotExist:
            raise NotFound("No feed found")
        polygons = feed.feed_polygons.all()

        rtsp_link = feed.rtsp_link

        current_timestamp = datetime.now()

        # Start the feed in a separate thread
        thread = threading.Thread(
            target=run, args=("yolov8n.pt",
                              'Shopping, People, Commerce, Mall, Many, Crowd, Walking   Free Stock video footage   YouTube.mp4', "cpu", True, [0], 2, 2, 2, event_id, feed_id, polygons, current_timestamp))
        thread.start()

        feed_status = FeedStatusModel(
            feed=feed, status="start", timestamp=current_timestamp)

        feed_status.save()
        return feed_status

    def stop_the_feed(self, client, event_id, feed_id):

        try:
            event = Event.objects.get(client=client, event_id=event_id)
        except Event.DoesNotExist:
            raise NotFound("No Event Found")

        try:
            feed = FeedModel.objects.get(event=event, feed_id=feed_id)
        except FeedModel.DoesNotExist:
            raise NotFound("No feed found")
        current_timestamp = datetime.now()
        stop_the_feed()
        # print("stop feed", stop_feed)

        feed_status = FeedStatusModel(
            feed=feed, status="stop", timestamp=current_timestamp)

        feed_status.save()
        return feed_status

    def get_all_feed_statuses(self):

        feed_statuses = FeedStatusModel.objects.all()

        return feed_statuses
