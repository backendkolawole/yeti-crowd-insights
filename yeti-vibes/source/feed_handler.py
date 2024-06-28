import json
from common import polygon_path
import cv2

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

    def verify_and_consume_rtsp(self, username=None, password=None):
        # Build the OpenCV video capture object
        cap = cv2.VideoCapture(self.rtsp_link)

        # Check if video capture object was created successfully
        if not cap.isOpened():
            print(f"Error opening RTSP stream: {self.rtsp_link}")
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

    def capture_and_display_frame(self):

        # Open the video capture device (e.g., webcam)
        cap = cv2.VideoCapture(self.rtsp_link)

        # Check if the video capture was successful
        if not cap.isOpened():
            print("Failed to open video capture device.")
            exit()

        # Main loop
        while True:
            # Read a frame from the video stream
            ret, frame = cap.read()

            # Check if the frame was read successfully
            if not ret:
                print("Failed to read a frame from the video stream.")
                break

            # Display the frame
            # print(ret, frame)
            cv2.imshow("Video Frame", frame)

            # Wait for the user to press 'q' to quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the video capture device and close all windows
        cap.release()
        cv2.destroyAllWindows()

    def process_feed(self):

        print(f"feed: {self.feed} is currently being processed, \n here is the rtsp link: {self.rtsp_link}")
        return self.verify_and_consume_rtsp(username=None, password=None)
    
    def get_frame(self):
        print(f"feed: {self.feed} \n here is the rtsp link for the video stream.: {self.rtsp_link}")
        return self.capture_and_display_frame()
    
    def my_method(self):
        print(f"feed = {self.feed}, rtsp = {self.rtsp_link}")
