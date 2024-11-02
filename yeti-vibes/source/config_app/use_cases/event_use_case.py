from config_app.repositories.event_repository import EventRepository


class EventUseCase:
    def __init__(self, repository: EventRepository):
        self.repository = repository

    def create_event(self, client, data):
        return self.repository.create_event(client=client, data=data)

    def get_all_events(self, client):
        return self.repository.get_all_events(client=client)

    def get_event(self, client, event_id):
        return self.repository.get_event(client=client, event_id=event_id)

    def update_event(self, client, event_id, data):
        return self.repository.update_event(client=client, event_id=event_id, data=data)

    def delete_event(self, client, event_id):
        return self.repository.delete_event(client=client, event_id=event_id)

    def start_the_event(self, client, event_id, feed_id):
        return self.repository.start_the_event(client=client, event_id=event_id, feed_id=feed_id)
    
    def stop_the_event(self, client, event_id, feed_id):
        return self.repository.stop_the_event(client=client, event_id=event_id, feed_id=feed_id)
    
    def get_all_event_statuses(self):
        return self.repository.get_all_event_statuses()
