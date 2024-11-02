# config_app/repositories/Feed_repository.py
from config_app.models import Feed as FeedModel, Event
from rest_framework.exceptions import NotFound
from config_app.models import Feed as FeedModel, FeedStatus as FeedStatusModel
from rest_framework.exceptions import NotFound
from datetime import datetime


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
            feed = FeedModel.objects.get(event_id=event_id, feed_id=feed_id)
        except FeedModel.DoesNotExist:
            raise NotFound("No Feed Found")

        polygons = feed.feed_polygons.all()

        rtsp_link = feed.rtsp_link

        current_timestamp = datetime.now()

        # return count_people_in_polygon(self.rtsp_link)
        run(
            weights="yolov8n.pt",
            source='Shopping, People, Commerce, Mall, Many, Crowd, Walking   Free Stock video footage   YouTube.mp4',
            device="cpu",
            view_img=True,
            classes=[0],
            line_thickness=2,
            track_thickness=2,
            region_thickness=2,
            event_id=event_id,
            feed_id=feed_id,
            polygons=polygons,
            timestamp=current_timestamp
        )

        feed_status = FeedStatusModel(
            feed_id=feed, status="start", timestamp=current_timestamp)

        feed_status.save()
        return feed_status

    def stop_the_feed(self, client, event_id, feed_id):
        try:
            feed = FeedModel.objects.get(event_id=event_id, feed_id=feed_id)
        except FeedModel.DoesNotExist:
            raise NotFound("No Feed Found")
        current_timestamp = datetime.now()

        feed_status = FeedStatusModel(
            feed_id=feed, status="stop", timestamp=current_timestamp)

        feed_status.save()
        return feed_status
    
    def get_all_feed_statuses(self):

        feed_statuses = FeedStatusModel.objects.all()

        return feed_statuses
