# Use-Case: 180 - Process the feed in real-time

## Goal

Receive a feed from the system, unpack its details. Start running and processing the feed. Pass the raw data to a queue for storage.

## Pre-Conditions

- A event has been started.
- It has complete feed details
- One or more polygons have been created for the feed
- RSTP link of the feed is working fine.

## Actors

- The system

## Entry Points

- [use-case: 150 - Start the event](150-Start_the_event.md)

## Main Flow (Triggered by Client)

1. Receive the feed details of one of the feeds of an event.
2. Verify if the feed details have an RSTP link
3. Verify if the feed details have the polygon details provided for the feed.
4. Define the polygon on the frame
5. Define the objects to be detected on the frame
6. Start the feed
7. print the detection details on the screen (for now).

## Secondary Flow (Triggered by Scheduler)

_TBD_

## Alternate Flow

## Exceptional Flow

## Implementation Details

### Class Description

- Create a class `FeedProcessor`.
- Create a function `process_the_feed` which takes a `Feed`object as parameter.
- *TBD - describe polygon boundaries*
- *TBD - define detections*
- *TBD - Load feed and provide above details*
- *TBD - Show/save detections*

### Reference
