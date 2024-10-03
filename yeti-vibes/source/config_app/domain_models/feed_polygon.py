class FeedPolygon:
    
    def __init__(self, polygon_id, feed_id, polygon_name, feed_polygons, polygon_color):
        
        self.polygon_id = polygon_id
        self.feed_id = feed_id
        self.polygon_name = polygon_name
        self.feed_polygons = feed_polygons
        self.polygon_color = polygon_color
        
        
    def __str__(self):
        return self.polygon_name
