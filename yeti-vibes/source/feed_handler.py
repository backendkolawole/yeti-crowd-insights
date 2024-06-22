import json
from common import polygon_path
from IPython.display import HTML
import cv2

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
        
    def verify_and_consume_rtsp(self, rtsp_link, username=None, password=None):
        # Build the OpenCV video capture object
        cap = cv2.VideoCapture(rtsp_link)

        # Check if video capture object was created successfully
        if not cap.isOpened():
            print(f"Error opening RTSP stream: {rtsp_link}")
            return False

        # Optional: Add username and password for authentication (if needed)
        if username and password:
            ret, frame = cap.read()
            while ret:
                # Check for frame validity (indicates successful authentication)
                if frame is None:
                    print("Failed to retrieve frame. Authentication might be required.")
                    cap.release()
                    return False
                ret, frame = cap.read()

            # Close the stream after checking authentication (optional cleanup)
            cap.release()
            cv2.destroyAllWindows()
            return False

        # Stream is accessible, start consuming frames
        while True:
            ret, frame = cap.read()

            # Check if frame is retrieved successfully
            if not ret:
                print("Error retrieving frame")
                break

            # Process the frame here (e.g., display, analyze)
            cv2.imshow("Video Stream", frame)

            # Exit loop if 'q' key is pressed
            if cv2.waitKey(1) == ord('q'):
                break

        # Release resources
        cap.release()
        cv2.destroyAllWindows()

        return True
    
    def process_feed(self):
        rtsp_link = self.feed['RTSPLink']
        print(f"feed: {self.feed} is currently being processed, \n here is the rtsp link: {rtsp_link}")
        return self.verify_and_consume_rtsp(rtsp_link)
    
        
    
    
        
        

