# config_app/repositories/FeedPolygonModel_repository.py
from config_app.models import Event, Feed, FeedPolygon as FeedPolygonModel
from config_app.domain_models.feed_polygon import FeedPolygon
from rest_framework.exceptions import NotFound


class FeedPolygonRepository:

    def create_feed_polygon(self, feed_id, event_id, client, data):
        try:
            event = Event.objects.get(client=client, event_id=event_id)
        except Event.DoesNotExist:
            raise NotFound("No Event Found")

        feed = Feed.objects.get(feed_id=feed_id, event=event)

        feed_polygon = FeedPolygonModel(feed=feed, **data)
        feed_polygon.save()
        return feed_polygon

    def get_all_feed_polygons(self, feed_id, event_id):
        try:
            event = Event.objects.get(event_id=event_id)
        except Event.DoesNotExist:
            raise NotFound("No Event Found")
        feed = Feed.objects.get(feed_id=feed_id, event=event)

        feed_polygons = FeedPolygonModel.objects.filter(feed=feed)

        return feed_polygons

    def get_feed_polygon(self, polygon_id, feed_id, event_id):
        try:
            event = Event.objects.get(event_id=event_id)
        except Event.DoesNotExist:
            raise NotFound("No Event Found")
        feed = Feed.objects.get(feed_id=feed_id, event=event)
        try:
            feed_polygon = FeedPolygonModel.objects.get(
                feed=feed, polygon_id=polygon_id)
        except FeedPolygonModel.DoesNotExist:
            raise NotFound("FeedPolygon matching query does not exist.")
        return feed_polygon

    def update_feed_polygon(self, polygon_id, feed_id, event_id, data):
        try:
            event = Event.objects.get(event_id=event_id)
        except Event.DoesNotExist:
            raise NotFound("No Event Found")
        feed = Feed.objects.get(feed_id=feed_id, event=event)
        try:
            feed_polygon = FeedPolygonModel.objects.get(
                feed=feed, polygon_id=polygon_id)
        except FeedPolygonModel.DoesNotExist:
            raise NotFound("FeedPolygon matching query does not exist.")

        for key, value in data.items():
            setattr(feed_polygon, key, value)
        feed_polygon.save()
        return feed_polygon

    def delete_feed_polygon(self, polygon_id, feed_id, event_id):
        try:
            event = Event.objects.get(event_id=event_id)
        except Event.DoesNotExist:
            raise NotFound("No Event Found")

        feed = Feed.objects.get(feed_id=feed_id, event=event)
        try:
            feed_polygon = FeedPolygonModel.objects.get(
                feed=feed, polygon_id=polygon_id)
        except FeedPolygonModel.DoesNotExist:
            raise NotFound("FeedPolygon matching query does not exist.")

        feed_polygon.delete()
        return {"success": True}
