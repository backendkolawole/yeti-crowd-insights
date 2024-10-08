# config_app/repositories/Feed_repository.py
from config_app.models import Feed as FeedModel, EventStatus as EventStatusModel
from rest_framework.exceptions import NotFound
from yolov8_region_counter import run
from datetime import datetime


class StartEventRepository:
    def count_in_polygon(self, event_id, feed_id):
        try:
            feed = FeedModel.objects.get(event_id=event_id, feed_id=feed_id)
        except FeedModel.DoesNotExist:
            raise NotFound("No Feed Found")
            
        feed_polygons = feed.feed_polygons.all()
        rtsp_link = feed.rtsp_link

        print(
            f"event_id: {event_id}, feed_id.: {feed_id}, rtsp_link: {rtsp_link}, feed_polygons: {feed_polygons}")

        # Get current timestamp
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
            feed_id=feed_id
        )
        
        event_status = EventStatusModel(event_id=event_id, event_status="start", timestamp=current_timestamp)
        
        event_status.save()
        print(event_status)
        return  event_status.id
