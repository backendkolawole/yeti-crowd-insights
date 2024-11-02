from config_app.domain_models.event import Event
from rest_framework.exceptions import NotFound
from config_app.models import EventStatus as EventStatusModel, Event as EventModel
from yolov8_region_counter import run
from datetime import datetime


class EventRepository:

    def create_event(self, client, data):
        event = EventModel(client=client, **data)
        event.save()
        return event

    def get_all_events(self, client):

        events = client.events.all()

        return events

    def get_event(self, client, event_id):
        try:
            event = EventModel.objects.get(client=client, event_id=event_id)

        except EventModel.DoesNotExist:
            raise NotFound("Event not found.")
        return event

    def update_event(self, client, event_id, data):
        try:
            event = EventModel.objects.get(client=client, event_id=event_id)

        except Event.DoesNotExist:
            raise NotFound("Event not found.")

        for key, value in data.items():
            setattr(event, key, value)
        event.save()

        return event

    def delete_event(self, client, event_id):
        try:
            event = EventModel.objects.get(client=client, event_id=event_id)
        except EventModel.DoesNotExist:
            raise NotFound("Event not found.")

        event.delete()
        return {"suceess"}
    
    def get_all_event_statuses(self):

        event_statuses = EventStatusModel.objects.all()

        return event_statuses


    # def start_the_event(self, client, event_id, feed_id):
    #     try:
    #         feed = FeedModel.objects.get(event_id=event_id, feed_id=feed_id)
    #     except FeedModel.DoesNotExist:
    #         raise NotFound("No Feed Found")

    #     polygons = feed.feed_polygons.all()

    #     rtsp_link = feed.rtsp_link

    #     current_timestamp = datetime.now()

    #     # return count_people_in_polygon(self.rtsp_link)
    #     run(
    #         weights="yolov8n.pt",
    #         source='Shopping, People, Commerce, Mall, Many, Crowd, Walking   Free Stock video footage   YouTube.mp4',
    #         device="cpu",
    #         view_img=True,
    #         classes=[0],
    #         line_thickness=2,
    #         track_thickness=2,
    #         region_thickness=2,
    #         event_id=event_id,
    #         feed_id=feed_id,
    #         polygons=polygons,
    #         timestamp=current_timestamp
    #     )

    #     try:
    #         event = EventModel.objects.get(client=client, event_id=event_id)
    #     except EventModel.DoesNotExist:
    #         raise NotFound("Event not found.")

    #     event_status = EventStatusModel(
    #         event_id=event, status="start", timestamp=current_timestamp)

    #     event_status.save()
    #     return event_status
    
    # def start_the_event(self, client, event_id, feed_id):
    #     try:
    #         feed = FeedModel.objects.get(event_id=event_id, feed_id=feed_id)
    #     except FeedModel.DoesNotExist:
    #         raise NotFound("No Feed Found")

    #     polygons = feed.feed_polygons.all()

    #     rtsp_link = feed.rtsp_link

    #     current_timestamp = datetime.now()

    #     # return count_people_in_polygon(self.rtsp_link)
    #     run(
    #         weights="yolov8n.pt",
    #         source='Shopping, People, Commerce, Mall, Many, Crowd, Walking   Free Stock video footage   YouTube.mp4',
    #         device="cpu",
    #         view_img=True,
    #         classes=[0],
    #         line_thickness=2,
    #         track_thickness=2,
    #         region_thickness=2,
    #         event_id=event_id,
    #         feed_id=feed_id,
    #         polygons=polygons,
    #         timestamp=current_timestamp
    #     )

    #     try:
    #         event = EventModel.objects.get(client=client, event_id=event_id)
    #     except EventModel.DoesNotExist:
    #         raise NotFound("Event not found.")

    #     event_status = EventStatusModel(
    #         event_id=event, status="start", timestamp=current_timestamp)

    #     event_status.save()
    #     return event_status
