# Use-Case: 160 - Load Feed Configuration

## Goal

The Feed configuration is loaded from the configuration file and returned to the calling use-case or function.

## Pre-Conditions

- A client detail record exists which holds the id and details of the clients
- One or more event record exists for a client, which hold the details of the events organized by that client.
- One or more feed configuration records exist, for each of the event, which holds the feed related information.
- One or more polygon configuration record exits, for each of the feed, which hold the polygon related details.

## Actors

- The system itself


## Entry Points
- Is triggered when the feed is started.
- Is triggered when the feed configuration data is requested.

## Main Flow
1. A call is received to load the feed configurations for an event.
2. The caller provides the event Id
    1. The caller provides a flag which asks to load:
        1. All the feeds.
        2. Only active marked feeds.
        3. Only inactive marked feeds.
3. The system creates a connection with the Feed configuration store
4. The system queries the store for all the feeds with that event id
5. The system fetches all the feed records for that event.
6. The system then queries for all the polygons for the feeds.
7. The system then fetches all the active polygons for that feed.
8. The system returns the array of feeds and polygons to the caller.

## Alternate Flow

## Exceptional Flow

## Implementation Details
### Class Description
#### `FeedPolygon` class
- Define a `FeedPolygon` class
- It should have the following properties:
    - `FeedId` as integer
    - `PolygonId` as integer
    - `PolygonName` as string
    - `Polygon` as list of vertices (can be provided to CV2 library)
    - `PolygonColor` as array of int, A BGR value'

#### `Feed` class
- Define a `Feed` class with the following properties:
    - `EventId` as integer
    - `FeedId` as integer
    - `FeedName` as string
    - `RTSPLink` as URL
    - an array of `FeedPolygon` objects
    - `IsActive` as Boolean
- Define a function in the class called `load_polygons`.
    - it should take `self.FeedId` as parameter and return and array of `FeedPolygon` objects


### Reference
- [An Ultralytics Example at GitHub using CV2](https://github.com/RizwanMunawar/ultralytics/blob/main/examples/YOLOv8-Region-Counter/yolov8_region_counter.py)
- [A Supervision/Roboflow example at GitHub](https://github.com/roboflow/supervision/blob/9b447296bfc18e937e7f11a90f95de5a7887feb6/supervision/draw/utils.py)
