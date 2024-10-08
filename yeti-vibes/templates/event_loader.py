import json
from feed_handler import FeedHandler


class Event:
    def __init__(self, event_id, feed_path):
        self.feeds = []
        self.event_id = event_id
        self.feed_path = feed_path

    def get_feeds(self):
        feed = FeedHandler(self.feed_path, self.event_id)
        feeds = feed.load_feeds()
        self.feeds = feeds
        return self.feeds


class EventLoader:
    def __init__(self, event_path, client_id):
        self.events = []
        self.event_path = event_path
        self.client_id = client_id

    def load_events(self):
        with open(self.event_path, 'r') as f:
            data = json.load(f)

        for event in data["event_config"]:
            if (event["Client Id"] == self.client_id):
                self.events.append(event)

        return self.events


# class Event:
#     def __init__(self, event_id, feed_path):
#         self.feeds = []
#         self.event_id = event_id
#         self.feed_path = feed_path

#     def get_feeds(self):
#         feed = FeedHandler(self.feed_path, self.event_id)
#         feeds = feed.load_feeds()
#         self.feeds = feeds
#         return self.feeds


# class EventLoader:
#     def __init__(self, event_path, client_id):
#         self.events = []
#         self.event_path = event_path
#         self.client_id = client_id

#     def load_events(self):
#         with open(self.event_path, 'r') as f:
#             data = json.load(f)

#         for event in data["event_config"]:
#             if (event["Client Id"] == self.client_id):
#                 self.events.append(event)

#         return self.events
