import json
from feed_handler import FeedHandler

class Event:
    def __init__(self):
        self.feeds = []

    def get_feeds(self, feed_path, event_id):
        feed = FeedHandler()
        self.feeds = feed.load_feeds(feed_path, event_id)
        return self.feeds
    

class EventLoader:
    def __init__(self):
        self.events = []

    def load_events(self, event_path, client_id):
        with open(event_path, 'r') as f:
            data = json.load(f)

        for event in data["event_config"]:
            if (event["Client Id"] == client_id):
                self.events.append(event)

        return self.events
