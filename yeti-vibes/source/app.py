from utils import process_feed
from event_loader import EventLoader

feed_path = '../json/feed_config.json'
polygon_path = '../json/feed_polygon.json'
event_path = '../json/event_config.json'
client_id = 1


class StartEvent:
    def __init__(self):
        self.processed_feeds = []

    def run_the_event(self, event_object):
        event_id = event_object["Event Id"]
        feeds = event_object.get_feeds(feed_path, event_id)
        for feed in feeds:
            processed_feed = process_feed(feed)
            self.processed_feeds.append(processed_feed)
            
        return self.processed_feeds
            

class ShowListOfEvents:
    def __init__(self):
        self.list_of_events = []

    # logic to load feeds and their polygons
    def show_list_of_events(self, event_path, client_id):
        event = EventLoader()
        data = event.load_events(event_path=event_path, client_id=client_id)
        self.list_of_events.append(data)
        
        return self.list_of_events
        
    
def main():

    # Create an instance of FeedHandler and FeedPolygon
    events = ShowListOfEvents()
    event_runner = StartEvent()
    
    running_events = []
    event_data = events.show_list_of_events(event_path, client_id)
    for event in event_data:
        running_events.append(event_runner.run_the_event(event))
    
    return running_events

# Call the main function
if __name__ == '__main__':
    main()
