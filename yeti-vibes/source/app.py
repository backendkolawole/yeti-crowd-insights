from camera_feed import FeedConfiguration, FeedPolygon

def main():

    # Create an instance of FeedConfiguration and FeedPolygon
    feed_config = FeedConfiguration()
    feed_polygon = FeedPolygon()



    # Call the display_details method
    print(feed_config.load_feed('../json/feed_config.json'))
    print(feed_polygon.load_polygon('../json/feed_polygon.json', 1))

# Call the main function
if __name__ == '__main__':
    main()
