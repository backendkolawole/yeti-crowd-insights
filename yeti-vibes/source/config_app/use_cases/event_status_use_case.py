from config_app.repositories.event_status_repository import EventStatusRepository


class EventStatusUseCase:
    def __init__(self, repository: EventStatusRepository):
        self.repository = repository

    def get_all_event_statuses(self):
        return self.repository.get_all_event_statuses()
