# config_app/repositories/Feed_repository.py
from config_app.models import Feed as FeedModel, Event
from rest_framework.exceptions import NotFound
from config_app.domain_models.feed import Feed



class FeedRepository:
    def create_feed(self, client, event_id, data):
        try:
            feed_event = Event.objects.get(client=client, event_id=event_id)
        except Event.DoesNotExist:
            raise NotFound("No Event Found")

        feed = FeedModel(event = feed_event, **data)
        feed.save()
        return Feed(feed_id=feed.feed_id, event=feed.event, feed_name=feed.feed_name, rtsp_link=feed.rtsp_link, is_active=feed.is_active)
    
    
    def get_all_feed(self, client, event_id):
        try:
            feed_event = Event.objects.get(
                client=client, event_id=event_id)
        except Event.DoesNotExist:
            raise NotFound("No Event Found")
        
        feeds = FeedModel.objects.filter(event = feed_event)
        
        return [Feed(feed_id = feed.feed_id, event = feed.event, feed_name = feed.feed_name, rtsp_link = feed.rtsp_link, is_active=feed.is_active) for feed in feeds]
    

    def get_feed(self, client, event_id, feed_id):
        try:
            feed_event = Event.objects.get(client = client, event_id=event_id)
        except Event.DoesNotExist:
            raise NotFound("No Event Found")

        try:
            feed = FeedModel.objects.get(event = feed_event, feed_id=feed_id)
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

        feed = FeedModel.objects.get(event = feed_event, feed_id =feed_id)
        feed.delete()
        return {"success"}
    
