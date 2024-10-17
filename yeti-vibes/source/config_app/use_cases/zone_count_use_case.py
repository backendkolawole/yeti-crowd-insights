from config_app.domain_models.zone_count import ZoneCount
from config_app.repositories.zone_count_repository import ZoneCountRepository


class ZoneCountUseCase:
    def __init__(self, repository: ZoneCountRepository):
        self.repository = repository

    def create_zone_count(self, event_id, polygon_id, count):
        zone_count = ZoneCount(event_id, polygon_id, count)
        return self.repository.create(zone_count)
