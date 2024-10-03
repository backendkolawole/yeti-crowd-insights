from config_app.repositories.feed_repository import FeedRepository


class FeedUseCase:
    def __init__(self, repository: FeedRepository):
        self.repository = repository

    def create_feed(self, client, event_id, data):
        return self.repository.create_feed(client = client, event_id = event_id, data=data)
    
    def get_all_feed(self, client, event_id):
        return self.repository.get_all_feed(client = client, event_id = event_id)

    def get_feed(self, client, event_id, feed_id):
        return self.repository.get_feed(client = client, event_id = event_id, feed_id=feed_id)

    def update_feed(self, client, event_id, feed_id, data):
        return self.repository.update_feed(client = client, event_id = event_id, feed_id=feed_id, data=data)

    def delete_feed(self, client, event_id, feed_id):
        return self.repository.delete_feed(client = client, event_id = event_id, feed_id=feed_id)