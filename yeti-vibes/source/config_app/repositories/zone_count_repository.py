# config_app/repositories/Feed_repository.py
from config_app.models import ZoneCount as ZoneCountModel
from rest_framework.exceptions import NotFound
from config_app.domain_models.zone_count import ZoneCount


class ZoneCountRepository:
    def exists(self, event_id, polygon_id):
        return ZoneCountModel.objects.filter(event_id=event_id, polygon_id=polygon_id).exists()
    

    def create_zone_count(self, zone_count):
        zone_count = ZoneCountModel(
            event_id=zone_count.event_id,
            polygon_id=zone_count.polygon_id,
            count=zone_count.count,
            timestamp=zone_count.timestamp  
        )
        zone_count.save()
        return zone_count
    

    def get_all_zone_counts(self, event_id, polygon_id):
        return ZoneCountModel.objects.filter(event_id=event_id, polygon_id=polygon_id)
    
    
        