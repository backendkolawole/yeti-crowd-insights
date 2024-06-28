from feed_handler import FeedProcessor
from event_loader import EventLoader, Event
from common import feed_path, event_path, client_id


class StartEvent:
    def __init__(self, event_object, feed_path):
        self.processed_feeds = []
        self.event_id = event_object["Event Id"]
        self.feed_path = feed_path

    def run_the_event(self):

        event = Event(self.feed_path, self.event_id)
        feeds = event.get_feeds()

        for feed_object in feeds:
            processor = FeedProcessor(feed_object)
            print(dir(processor))
            return processor.process_feed()

    def count_the_objects(self):
        # processor = FeedProcessor(feed_object)

        # return processor.process_feed()
        pass


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
        return event_runner.run_the_event()


# Call the main function
if __name__ == '__main__':
    main()
