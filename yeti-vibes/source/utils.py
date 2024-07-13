import cv2
from ultralytics import YOLO, solutions

import numpy as np

def capture_and_display_frame(rtsp_link):

    # Open the video capture device (e.g., webcam)
    cap = cv2.VideoCapture(rtsp_link)

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
            print("Failed to read a frame from the video stream")
            break

        # Display the frame
        # print(ret, frame)
        # cv2.imwrite("frame.jpg", frame)
        cv2.imshow("Video Frame", frame)

        # Wait for the user to press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture device and close all windows
    cap.release()
    cv2.destroyAllWindows()


def detect_and_track_objects(rtsp_link):

    # Load the YOLOv8 model
    model = YOLO("yolov8n.pt")

    # Open the video file
    cap = cv2.VideoCapture(rtsp_link)

    if not cap.isOpened():
        print("Failed to open video capture device.")
        exit()

    # Loop through the video frames
    while cap.isOpened():
        print('cap is opened')
        # Read a frame from the video
        success, frame = cap.read()

        if success:
            # Run YOLOv8 tracking on the frame, persisting tracks between frames
            results = model.track(frame, persist=True)
            # Visualize the results on the frame
            annotated_frame = results[0].plot()

            # Display the annotated frame
            cv2.imshow("YOLOv8 Tracking", annotated_frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            # Break the loop if the end of the video is reached
            break

    # Release the video capture object and close the display window
    cap.release()
    cv2.destroyAllWindows()


def count_people_in_region(rtsp_link):
    """Count objects in a specific region within a video."""

    # Load the YOLOv8 model
    model = YOLO("yolov8n.pt")
    # Open the video file
    cap = cv2.VideoCapture(rtsp_link)

    assert cap.isOpened(), "Error reading video file"
    w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH,
                 cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

    # Define region points
    region_points = [(321, 241), (813, 237)]

    classes_to_count = [0]  # person classes for count

    # Video writer
    video_writer = cv2.VideoWriter(
        "object_counting_output.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

    # Init Object Counter
    counter = solutions.ObjectCounter(
        view_img=True,
        reg_pts=region_points,
        classes_names=model.names,
        draw_tracks=True,
        line_thickness=2
    )

    while cap.isOpened():
        success, im0 = cap.read()
        if not success:
            print(
                "Video frame is empty or video processing has been successfully completed.")
            break
        tracks = model.track(im0, persist=True, show=False,
                             classes=classes_to_count)

        im0 = counter.start_counting(im0, tracks)
        video_writer.write(im0)

    cap.release()
    video_writer.release()
    cv2.destroyAllWindows()


def count_people_in_polygon(rtsp_link):
    """Count objects in a specific region within a video."""

    # Load the YOLOv8 model
    model = YOLO("yolov8n.pt")
    # Open the video file
    cap = cv2.VideoCapture(rtsp_link)

    assert cap.isOpened(), "Error reading video file"
    w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH,
                 cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

    # Define region points as a polygon with 5 points
    # region_points = [(20, 400), (1080, 404), (1080, 360), (20, 360), (20, 400)]
    region_points = [(402, 166), (458, 338), (370, 394), (
        226, 398), (210, 182), (390, 158), (398, 162), (394, 170)]
    classes_to_count = [0]  # person classes for count

    # Video writer
    video_writer = cv2.VideoWriter(
        "object_counting_output.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

    # Init Object Counter
    counter = solutions.ObjectCounter(
        view_img=True,
        reg_pts=region_points,
        classes_names=model.names,
        draw_tracks=True,
        line_thickness=2
    )

    while cap.isOpened():
        success, im0 = cap.read()
        if not success:
            print(
                "Video frame is empty or video processing has been successfully completed.")
            break
        tracks = model.track(im0, persist=True, show=False,
                             classes=classes_to_count)

        im0 = counter.start_counting(im0, tracks)
        # video_writer.write(im0)

    cap.release()
    video_writer.release()
    cv2.destroyAllWindows()
    

def generate_heatmaps(rtsp_link):

    model = YOLO("yolov8n.pt")
    cap = cv2.VideoCapture(rtsp_link)
    assert cap.isOpened(), "Error reading video file"
    w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH,
                cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

    classes_for_heatmap = [0]  # classes for heatmap

    # Init heatmap
    heatmap_obj = solutions.Heatmap(
        colormap=cv2.COLORMAP_PARULA,
        view_img=True,
        shape="circle",
        classes_names=model.names,
    )

    while cap.isOpened():
        success, im0 = cap.read()
        if not success:
            print("Video frame is empty or video processing has been successfully completed.")
            break
        tracks = model.track(im0, persist=True, show=False,
                            classes=classes_for_heatmap)

        im0 = heatmap_obj.generate_heatmap(im0, tracks)

    cap.release()
    cv2.destroyAllWindows()
    
# count_people_in_region(rtsp_link='Shopping, People, Commerce, Mall, Many, Crowd, Walking   Free Stock video footage   YouTube.mp4')
generate_heatmaps(
    rtsp_link='Shopping, People, Commerce, Mall, Many, Crowd, Walking   Free Stock video footage   YouTube.mp4')
