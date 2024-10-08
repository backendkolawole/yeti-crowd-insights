# config_app/repositories/Feed_repository.py
from config_app.models import Feed as FeedModel, EventStatus as EventStatusModel
from config_app.domain_models.event_status import EventStatus
from rest_framework.exceptions import NotFound
from yolov8_region_counter import run
from datetime import datetime
from rest_framework.response import Response 

class EventStatusRepository:
    def get_all_event_statuses(self):
        
        event_statuses = EventStatusModel.objects.all()
        
        result = [EventStatus(event_id=event_status.event_id, status=event_status.status,
                              timestamp=event_status.timestamp) for event_status in event_statuses]

        return Response({"event_statuses": result})

