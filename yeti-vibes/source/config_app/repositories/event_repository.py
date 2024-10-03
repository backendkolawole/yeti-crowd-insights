# config_app/repositories/Event_repository.py
from config_app.models import Event as ModelEvent
from config_app.domain_models.event import Event
from rest_framework.exceptions import NotFound


class EventRepository:
    
    def create_event(self, client, data):
        event = ModelEvent(client=client, **data)
        event.save()
        return Event(event_id=event.event_id, client = event.client, event_name = event.event_name, description=event.description, start_date = event.start_date, end_date = event.end_date, is_active = event.is_active)
    
    def get_all_events(self, client):
        
        events = ModelEvent.objects.filter(client=client)
        
        return [Event(event_id=event.event_id, client = event.client, event_name = event.event_name, description=event.description, start_date = event.start_date, end_date = event.end_date, is_active = event.is_active) for event in events]

    def get_event(self, client, event_id):
        try:
            event = ModelEvent.objects.get(client = client, event_id=event_id)
            
        except Event.DoesNotExist:
            raise NotFound("Client not found.")
        return Event(event_id=event.event_id, client=event.client, event_name=event.event_name, description=event.description, start_date=event.start_date, end_date=event.end_date, is_active=event.is_active)
        # return Event.objects.get(id=xlient_id)



    def update_event(self, client, event_id, data):
        try:
            event = ModelEvent.objects.get(client=client, event_id=event_id)
        
        except Event.DoesNotExist:
            raise NotFound("Client not found.")
            
        for key, value in data.items():
            setattr(event, key, value)
        event.save()
        
        return Event(
            event_id = event.event_id,
            client = event.client,
            event_name = event.event_name,
            description = event.description,
            start_date = event.start_date,
            end_date = event.end_date,
            is_active = event.is_active
        )

    def delete_event(self, client, event_id):
        try:
            event = ModelEvent.objects.get(client = client, event_id=event_id)
        except Event.DoesNotExist:
            raise NotFound("Client not found.")

        event.delete()
        return {"suceess"}
    
