from config_app.repositories.start_event_repository import StartEventRepository


class StartEventUseCase:
    def __init__(self, repository: StartEventRepository):
        self.repository = repository

    def count_in_polygon(self, event_id, feed_id):
        return self.repository.count_in_polygon(event_id=event_id, feed_id=feed_id)