from feed_handler import FeedHandler, FeedPolygon

feed_path = '../json/feed_config.json'
polygon_path = '../json/feed_polygon.json'
event_path = '../json/event_config.json'

class FeedProcessor:
    def __init__(self):
        self.processed_feed = []

    # logic to load feeds and their polygons
    def process_the_feed(self, feed_object):
        pass
    
def main():

    # Create an instance of FeedHandler and FeedPolygon
    feed_config = FeedHandler()
    feed_polygon = FeedPolygon()

    # Call the display_details method
    print(feed_config.load_feeds(feed_path=feed_path, event_id=1))
    print(feed_polygon.load_polygons(feed_id=1, polygon_path=polygon_path))



# Call the main function
if __name__ == '__main__':
    main()
