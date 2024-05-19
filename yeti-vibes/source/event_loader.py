import json
from feed_handler import FeedHandler, FeedProcessor

#  use-case "145 - Show List of events"
class Event:
    def __init__(self):
        self.feeds = []

    def get_feeds(self, feed_path, event_id):
        feed = FeedHandler()
        self.feeds = feed.load_feeds(feed_path, event_id)
        return self.feeds
    

#  use-case "145 - Show List of events"
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

class StartEvent:
    def __init__(self):
        pass
    
    def run_the_event(self, event_object):
        feed = event_object.get_feeds(feed_path=feed_path, event_id=event_id)
        
        feed_processor = FeedProcessor()
        feed_processor.process_the_feed(feed_object=feed)
