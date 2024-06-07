from feed_handler import FeedProcessor
from event_loader import EventLoader, Event
from common import feed_path, event_path, client_id



class StartEvent:
    def __init__(self):
        self.processed_feeds = []

    def run_the_event(self, event_list):
        for event_item in event_list:
            event_id = event_item["Event Id"]
            
            event = Event()
            feeds = event.get_feeds(feed_path, event_id)
            for feed in feeds:
                processor = FeedProcessor(feed)
                processed_feed = processor.process_feed()
                self.processed_feeds.append(processed_feed)
                
            return self.processed_feeds
            

class ShowListOfEvents:
    def __init__(self):
        self.list_of_events = []

    # logic to show list of events
    def show_list_of_events(self, event_path= event_path, client_id=client_id):
        event = EventLoader()
        data = event.load_events(event_path=event_path, client_id=client_id)
        self.list_of_events.append(data)
        
        return self.list_of_events
        
    
def main():

    running_events = []
    events = ShowListOfEvents()
    event_runner = StartEvent()
    
    event_data = events.show_list_of_events(event_path, client_id)
    
    for event in event_data:
        running_events.append(event_runner.run_the_event(event))
        
    
    
    return running_events

# Call the main function
if __name__ == '__main__':
    main()
