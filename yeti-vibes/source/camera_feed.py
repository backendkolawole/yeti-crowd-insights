import json

class FeedPolygon:
    def __init__(self):
        self.feed_polygons = []

    def load_polygon(self, polygon_path, feed_id):
        # logic to load the data on the basis of feed_id
    
        with open(polygon_path, 'r') as f:
            data = json.load(f)
            
            
        for polygon in data["feed_polygon"]:
            # print(polygon)
            if (polygon['FeedId'] == feed_id):
                self.feed_polygons.append(polygon)
        
        return self.feed_polygons
    
    
class FeedConfiguration:
    def __init__(self):
        self.feed = []

    # logic to load feeds and their polygons
    def load_feed(self, feed_path):
        
        with open(feed_path, 'r') as f:
            data = json.load(f)
            self.feed = data
        return self.feed
    
    
    
    
# polygons = FeedPolygon.load_polygon(polygonPath, feedId)
# FeedConfiguration.polygons[0].polygondid
# FeedConfiguration.polygons[0].name
# FeedConfiguration.polygons[1]





# # Get camera feeds from a configuration file or database


# class LoadFeedConfiguration:
#     def __init__(self, event):
#         """
#         Initializes a CameraFeed object with an event.

#         Args:
#             event: The event associated with the camera feed.

#         Returns:
#             None
#         """
#         self.event = event

#     # def load_feed_configurations(self):
#     def load_feed_configurations(self, property1, property2):
#         # feed

    
    
    
#         # self.feed_config = []
#         self.feed_config = []

#         """
#         Load all the Feed configurations for a given event.

#         Parameters:
#         - event: The event for which to load the Feed configurations.

#         Returns:
        
#         an array of feed configurations

#         Description:
#         This method loads all the Feed configurations for a given event and stores them in the structure FeedConfigurations.
#         """

#         with open(self.event, 'r') as f:
#             data = json.load(f)
#             self.config = data

#         # print(data)
#         return self.config

#     def load_feed_polygons(self):
#         self.feed_polygons = []
#         """
#         Load all the polygon configuration for the event.

#         Args:
#             event: The event for which the polygon configuration is being loaded.

#         Returns:
#             list: A list of polygon configurations for the event.
#         """

#         with open(self.event, 'r') as f:
#             data = json.load(f)

#         for i in data["feed_polygon"]:
#             self.feed_polygons.append(i)
#             # print(self.feed_polygons)
#             return self.feed_polygons























# # # Get camera feeds from a configuration file or database

# # class CameraFeed:
# #     def __init__(self, camera_id, rstp_url):
# #         # Initialize CameraFeed object with ID and RSTP URL
# #         self.camera_id = camera_id
# #         self.rstp_url = rstp_url

# #     def read_frame(self):
# #         # Read frame from the camera feed
# #         # Placeholder logic, actual implementation depends on your camera feed source
# #         pass

# # class CameraFeedProcessor:
# #     def __init__(self):
# #         # Initialize CameraFeedProcessor
# #         self.camera_feeds = []

# #     def get_camera_feeds(self):
# #         # Fetch camera feeds from configuration or database
# #         # Placeholder logic, actual implementation depends on your camera feed source
# #         return self.camera_feeds