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
    region_points = [(50, 80), (250, 20), (450, 80), (400, 350), (100, 350)]

    classes_to_count = [0]  # person classes for count

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
    
def run(
    weights="yolov8n.pt",
    source=None,
    device="cpu",
    view_img=False,
    classes=None,
    line_thickness=2,
    track_thickness=2,
    region_thickness=2,
):
    """
    Run Region counting on a video using YOLOv8 and ByteTrack.

    Supports movable region for real time counting inside specific area.
    Supports multiple regions counting.
    Regions can be Polygons or rectangle in shape

    Args:
        weights (str): Model weights path.
        source (str): Video file path.
        device (str): processing device cpu, 0, 1
        view_img (bool): Show results.
        save_img (bool): Save results.
        exist_ok (bool): Overwrite existing files.
        classes (list): classes to detect and track
        line_thickness (int): Bounding box thickness.
        track_thickness (int): Tracking line thickness
        region_thickness (int): Region thickness.
    """
    vid_frame_count = 0

    # Check source path
    if not Path(source).exists():
        raise FileNotFoundError(f"Source path '{source}' does not exist.")

    # Setup Model
    model = YOLO(f"{weights}")
    model.to("cuda") if device == "0" else model.to("cpu")

    # Extract classes names
    names = model.model.names

    # Video setup
    videocapture = cv2.VideoCapture(source)

    region_points = [(50, 80), (250, 20), (450, 80), (400, 350), (100, 350)]

    # Init Object Counter
    counter = solutions.ObjectCounter(
        view_img=True,
        reg_pts=region_points,
        classes_names=model.names,
        draw_tracks=True,
        line_thickness=2
    )

    # Iterate over video frames
    while videocapture.isOpened():
        success, frame = videocapture.read()
        if not success:
            break
        vid_frame_count += 1

        # Extract the results
        results = model.track(frame, persist=True, classes=classes)
        # frame = counter.start_counting(frame, results)

        if results[0].boxes.id is not None:
            print(f"id is not none", results[0].boxes)
            boxes = results[0].boxes.xyxy.cpu()
            track_ids = results[0].boxes.id.int().cpu().tolist()
            clss = results[0].boxes.cls.cpu().tolist()

            annotator = Annotator(
                frame, line_width=line_thickness, example=str(names))

            for box, track_id, cls in zip(boxes, track_ids, clss):
                annotator.box_label(
                    box, str(names[cls]), color=colors(cls, True))
                bbox_center = (box[0] + box[2]) / \
                    2, (box[1] + box[3]) / 2  # Bbox center

                track = track_history[track_id]  # Tracking Lines plot
                track.append((float(bbox_center[0]), float(bbox_center[1])))
                if len(track) > 30:
                    track.pop(0)
                points = np.hstack(track).astype(np.int32).reshape((-1, 1, 2))
                cv2.polylines(frame, [points], isClosed=False, color=colors(
                    cls, True), thickness=track_thickness)

                # Check if detection inside region
                for region in counting_regions:
                    if region["polygon"].contains(Point((bbox_center[0], bbox_center[1]))):
                        region["counts"] += 1

        # Draw regions (Polygons/Rectangles)
        for region in counting_regions:
            print(region)
            region_label = str(region["counts"])
            region_color = region["region_color"]
            region_text_color = region["text_color"]

            polygon_coords = np.array(
                region["polygon"].exterior.coords, dtype=np.int32)
            centroid_x, centroid_y = int(region["polygon"].centroid.x), int(
                region["polygon"].centroid.y)

            text_size, _ = cv2.getTextSize(
                region_label, cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.7, thickness=line_thickness
            )
            text_x = centroid_x - text_size[0] // 2
            text_y = centroid_y + text_size[1] // 2
            cv2.rectangle(
                frame,
                (text_x - 5, text_y - text_size[1] - 5),
                (text_x + text_size[0] + 5, text_y + 5),
                region_color,
                -1,
            )
            cv2.putText(
                frame, region_label, (
                    text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, region_text_color, line_thickness
            )
            cv2.polylines(frame, [polygon_coords], isClosed=True,
                          color=region_color, thickness=region_thickness)

        if view_img:
            if vid_frame_count == 1:
                cv2.namedWindow("Ultralytics YOLOv8 Region Counter Movable")
                cv2.setMouseCallback(
                    "Ultralytics YOLOv8 Region Counter Movable", mouse_callback)
            cv2.imshow("Ultralytics YOLOv8 Region Counter Movable", frame)

        for region in counting_regions:  # Reinitialize count for each region
            region["counts"] = 0

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    del vid_frame_count
    videocapture.release()
    cv2.destroyAllWindows()
    
    
# count_people_in_polygon(rtsp_link='Shopping, People, Commerce, Mall, Many, Crowd, Walking   Free Stock video footage   YouTube.mp4')    
# count_people_in_region(rtsp_link='Shopping, People, Commerce, Mall, Many, Crowd, Walking   Free Stock video footage   YouTube.mp4')
# generate_heatmaps(
#     rtsp_link='Shopping, People, Commerce, Mall, Many, Crowd, Walking   Free Stock video footage   YouTube.mp4')
