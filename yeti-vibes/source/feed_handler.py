from common import polygon_path
from feed_utils import capture_and_display_frame, count_people_in_region, detect_and_track_objects
import json
from yolov8_region_counter import run 

# Use-Case: 160 - Load Feed Configuration


class Feed:
    def __init__(self, feed_id, polygon_path):
        self.feed_polygons = []
        self.feed_id = feed_id
        self.polygon_path = polygon_path

    def load_polygons(self):
        # logic to load the data on the basis of feed_id

        with open(polygon_path, 'r') as f:
            data = json.load(f)

        for polygon in data["feed_polygon"]:
            if (polygon['FeedId'] == self.feed_id):
                self.feed_polygons.append(polygon)

        return self.feed_polygons


# Use-Case: 160 - Load Feed Configuration
class FeedHandler:
    def __init__(self, event_id, feed_path):
        self.feed = []
        self.event_id = event_id
        self.feed_path = feed_path

    # logic to load feeds and their polygons
    def load_feeds(self):

        with open(self.feed_path, 'r') as f:
            data = json.load(f)

        for feed_item in data["feed_config"]:
            if (feed_item["EventId"] == self.event_id):
                matching_feed = feed_item
                feed_id = matching_feed["FeedId"]
                feed = Feed(feed_id, polygon_path)
                feed_polygons = feed.load_polygons()
                matching_feed['Polygons'] = feed_polygons
                self.feed.append(matching_feed)
        return self.feed


class FeedProcessor:
    def __init__(self, feed_object):
        self.feed = feed_object
        self.rtsp_link = self.feed['RTSPLink']

    def get_frame(self):
        print(f"feed: {self.feed} \n here is the rtsp link for the video stream.: {self.rtsp_link}")
        return capture_and_display_frame(self.rtsp_link)

    def detect_objects(self):
        print(f"feed: {self.feed} \n here is the rtsp link for the video stream.: {self.rtsp_link}")
        return detect_and_track_objects(self.rtsp_link)
    
    def count_in_region(self):
        print(f"feed: {self.feed} \n here is the rtsp link for the video stream.: {self.rtsp_link}")
        return count_people_in_region(self.rtsp_link)
    
    def count_in_polygon(self):
        print(f"feed: {self.feed} \n here is the rtsp link for the video stream.: {self.rtsp_link}")
        # return count_people_in_polygon(self.rtsp_link)
        return run(
            weights="yolov8n.pt",
            source='Shopping, People, Commerce, Mall, Many, Crowd, Walking   Free Stock video footage   YouTube.mp4',
            device="cpu",
            view_img=True,
            classes=[0],
            line_thickness=2,
            track_thickness=2,
            region_thickness=2,
        )

