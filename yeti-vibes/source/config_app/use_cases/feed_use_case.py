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
    
    def configure_zones_on_frame(self):
        pass

    def provide_camera_feed_details(self):
        pass

    def update_feed(self):
        pass

    def delete_feed(self):
        pass

    def process_the_feed(self):
        pass

    def load_feed_configuration(self, feed):
        pass

    def run_video_feed(self, feed):
        pass

    def detect_and_identify_the_person(self, data):
        pass

    def capture_the_reaction(self, data):
        pass

    def handle_the_payment(self, data):
        pass

    def generate_insights(self, data):
        pass

    def validate_the_reaction(self, data):
        pass

    def save_the_reaction(self, data):
        pass
