import psycopg2
import time
import mediapipe as mp
import cv2
from datetime import datetime


BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode


targets = {
    "Thumb_Down": 3,
    "Thumb_Up": 4,
}

last_gesture = 0

def save_gesture(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    global last_gesture
    
    # connect to a postgresql database server
    # conn = psycopg2.connect(database="yeti-crowd-insights",
    #                         user="postgres",
    #                         host='localhost',
    #                         password="1Aa@36052546postgres",
    #                         port=5432)

    # Open a cursor to perform database operations
    # cur = conn.cursor()
    
    if result.gestures:
        # print(result)
        gesture = result.gestures[0][0].category_name

        if gesture and gesture in targets:
            if last_gesture != gesture or last_gesture == 0:
                last_gesture = gesture
                print(gesture)
                
                # Insert data
                current_timestamp = datetime.now()
                sql = f"""INSERT INTO gestures (feed_id, gesture, person_id,0 ts)
                                VALUES (
                                    '1', '{gesture}', '{current_timestamp}')
                                """
                # cur.execute(sql)
    
    # conn.commit()
    # cur.close()
    # conn.close()
                


options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path='gesture_recognizer.task'),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=save_gesture)


recognizer = GestureRecognizer.create_from_options(options)


prev_timestamp_ms = 0

def detect_gesture():
    
    # For webcam input:
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        # Capture a frame from the camera
        ret, frame = cap.read()

        # Check if the frame was captured successfully
        if not ret:
            print("Failed to capture a frame")
            break

        # Get the current timestamp in milliseconds
        current_timestamp_ms = int(time.time() * 1000)

        # Check if the timestamp is monotonically increasing
        if current_timestamp_ms > prev_timestamp_ms:

            # Convert the frame received from OpenCV to a MediaPipe’s Image object.
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
            recognizer.recognize_async(mp_image, current_timestamp_ms)

        # Display the captured frame
        cv2.imshow('Camera Feed', frame)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()


detect_gesture()
