from feed_handler import FeedProcessor



def process_feed(feed):
    processor = FeedProcessor(feed)
    processor.process()


