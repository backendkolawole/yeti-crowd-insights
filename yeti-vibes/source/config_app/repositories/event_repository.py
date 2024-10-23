# config_app/repositories/Event_repository.py
from config_app.models import Event as EventModel
from config_app.domain_models.event import Event
from rest_framework.exceptions import NotFound


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
        except Event.DoesNotExist:
            raise NotFound("Event not found.")

        event.delete()
        return {"suceess"}
