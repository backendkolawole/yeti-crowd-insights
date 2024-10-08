# from yolo8 import YOLO8
from feed_handler import FeedProcessor
from event_loader import EventLoader, Event
from common import feed_path, event_path, client_id


class StartEvent:
    def __init__(self, event_object, feed_path):
        self.processed_feeds = []
        self.event_id = event_object["Event Id"]
        self.feed_path = feed_path


    # def display_a_frame(self):
    #     event = Event(self.feed_path, self.event_id)
    #     feeds = event.get_feeds()
        
    #     for feed_object in feeds:
    #         processor = FeedProcessor(feed_object)
    #         # print(type(processor))
    #         return processor.get_frame()
    
    # def detect_the_objects(self):
    #     event = Event(self.feed_path, self.event_id)
    #     feeds = event.get_feeds()

    #     for feed_object in feeds:
    #         processor = FeedProcessor(feed_object)
    #         # print(type(processor))
    #         return processor.detect_objects()
    
    # def count_in_region(self):
    #     event = Event(self.feed_path, self.event_id)
    #     feeds = event.get_feeds()

    #     for feed_object in feeds:
    #         processor = FeedProcessor(feed_object)
    #         # print(type(processor))
    #         return processor.count_in_region()
    
    def count_in_polygon(self):
        event = Event(self.feed_path, self.event_id)
        feeds = event.get_feeds()

        for feed_object in feeds:
            processor = FeedProcessor(feed_object)
            # print(type(processor))
            return processor.count_in_polygon()


class ShowListOfEvents:
    def __init__(self, event_path, client_id):
        self.list_of_events = []
        self.event_path = event_path
        self.client_id = client_id

    # logic to show list of events
    def show_list_of_events(self):
        event = EventLoader(event_path, client_id)
        self.list_of_events = event.load_events()
        return self.list_of_events



def main():

    events = ShowListOfEvents(event_path, client_id)
    event_list = events.show_list_of_events()

    for event_object in event_list:
        event_runner = StartEvent(event_object, feed_path)
        # return event_runner.display_a_frame()
        # return event_runner.detect_the_objects()
        # return event_runner.count_in_region()
        return event_runner.count_in_polygon()





# Call the main function
if __name__ == '__main__':
    main()
