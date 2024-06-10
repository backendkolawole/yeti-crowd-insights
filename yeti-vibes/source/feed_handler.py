import json
from common import polygon_path
from IPython.display import HTML, Video, IFrame
import time

# Use-Case: 160 - Load Feed Configuration
class Feed:
    def __init__(self):
        self.feed_polygons = []

    def load_polygons(self, feed_id, polygon_path):
        # logic to load the data on the basis of feed_id

        with open(polygon_path, 'r') as f:
            data = json.load(f)

        for polygon in data["feed_polygon"]:
            if (polygon['FeedId'] == feed_id):
                self.feed_polygons.append(polygon)
                
        return self.feed_polygons
    
    
# Use-Case: 160 - Load Feed Configuration
class FeedHandler:
    def __init__(self):
        self.feed = []

    # logic to load feeds and their polygons
    def load_feeds(self, feed_path, event_id):
        
        with open(feed_path, 'r') as f:
            data = json.load(f)
        
        for feed_item in data["feed_config"]:
            if (feed_item["EventId"] == event_id):   
                matching_feed = feed_item
                feed_id = matching_feed["FeedId"]                
                feed = Feed()
                feed_polygons = feed.load_polygons(feed_id=feed_id, polygon_path=polygon_path)
                matching_feed['Polygons'] = feed_polygons
                self.feed.append(matching_feed)
        return self.feed
        

class FeedProcessor:
    def __init__(self, feed):
        self.feed = feed
        

    def process_feed(self):
        rtsp_link = self.feed['RTSPLink']
        print(f"feed: {self.feed} is currently being processed, \n here is the rtsp link: {rtsp_link}")
        # return HTML(f'<video width="640" height="360" controls><source src="{rtsp_link}" type="video/mp4">Your browser does not support the video tag.</video>')
        video_html = f'''
        <img src="{rtsp_link}" width="640" height="480" alt="Motion JPEG Video Stream">
        '''


        # Display the video stream
        HTML(video_html)
                
    
    
        
        

