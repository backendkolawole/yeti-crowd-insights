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
    
    

# # the applicaiton start-up code
# from camera_feed import LoadFeedConfiguration
# from camera_feed import CameraFeedProcessor
# from gesture_detector import GestureDetector
# from database import Database

# class MicroSaaSApplication:
#     def __init__(self):
#         # Initialize components
#         self.camera_feed_processor = CameraFeedProcessor()
#         self.gesture_detector = GestureDetector()
#         self.database = Database()

#     def run(self):
#         # Continuously process camera feeds and detect gestures
#         while True:
#             camera_feeds = self.camera_feed_processor.get_camera_feeds()
#             for camera_feed in camera_feeds:
#                 frame = camera_feed.read_frame()
#                 gesture = self.gesture_detector.detect_gesture(frame)
#                 if gesture:
#                     self.database.save_gesture(gesture, camera_feed.camera_id)


# if __name__ == "__main__":
#     # Start the application
#     app = MicroSaaSApplication()
#     app.run()