from feed_handler import FeedProcessor
from event_loader import EventLoader, Event
from common import feed_path, event_path, client_id


class StartEvent:
    def __init__(self):
        self.processed_feeds = []

    def run_the_event(self, event_object):
        event_id = event_object["Event Id"]

        event = Event()
        feeds = event.get_feeds(feed_path, event_id)

        for feed in feeds:
            processor = FeedProcessor(feed)
            return processor.process_feed()


class ShowListOfEvents:
    def __init__(self):
        self.list_of_events = []

    # logic to show list of events
    def show_list_of_events(self, event_path=event_path, client_id=client_id):
        event = EventLoader()
        data = event.load_events(event_path=event_path, client_id=client_id)
        return data


def main():

    events = ShowListOfEvents()
    event_runner = StartEvent()

    event_list = events.show_list_of_events(event_path, client_id)

    for event in event_list:
        return event_runner.run_the_event(event)


# Call the main function
if __name__ == '__main__':
    main()
