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
