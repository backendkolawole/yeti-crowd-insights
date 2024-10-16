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
        
        return event_statuses

