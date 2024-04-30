import json

# Get camera feeds from a configuration file or database

class LoadFeedConfiguration:
    def __init__(self, event):
        """
        Initializes a CameraFeed object with an event.

        Args:
            event: The event associated with the camera feed.

        Returns:
            None
        """
        self.event = event
        
    def load_feed_configurations(self):
        """
        Load all the Feed configurations for a given event.

        Parameters:
        - event: The event for which to load the Feed configurations.

        Returns:
        None

        Description:
        This method loads all the Feed configurations for a given event and stores them in the structure FeedConfigurations.
        """
        
        with open(self.event, 'r') as f:
            data = json.load(f)
        
        print(data)



    def load_feed_polygons(self):
        self.feed_polygons = []
        """
        Load all the polygon configuration for the event.

        Args:
            event: The event for which the polygon configuration is being loaded.

        Returns:
            list: A list of polygon configurations for the event.
        """
        
        with open(self.event, 'r') as f:
            data = json.load(f)
        
        for i in data["feed_polygon"]:
            self.feed_polygons.append(i)
        print(self.feed_polygons)
    
def main():
    
    print('getting to this point')
    # Create an instance of LoadFeedConfiguration
    feed_config = LoadFeedConfiguration("./json/feed_config.json")
    feed_polygon = LoadFeedConfiguration("./json/feed_polygon.json")

    # Call the display_details method
    feed_config.load_feed_configurations()
    feed_polygon.load_feed_polygons()
    

# Call the main function
if __name__ == '__main__':
    main()



# # Get camera feeds from a configuration file or database

# class CameraFeed:
#     def __init__(self, camera_id, rstp_url):
#         # Initialize CameraFeed object with ID and RSTP URL
#         self.camera_id = camera_id
#         self.rstp_url = rstp_url

#     def read_frame(self):
#         # Read frame from the camera feed
#         # Placeholder logic, actual implementation depends on your camera feed source
#         pass

# class CameraFeedProcessor:
#     def __init__(self):
#         # Initialize CameraFeedProcessor
#         self.camera_feeds = []

#     def get_camera_feeds(self):
#         # Fetch camera feeds from configuration or database
#         # Placeholder logic, actual implementation depends on your camera feed source
#         return self.camera_feeds