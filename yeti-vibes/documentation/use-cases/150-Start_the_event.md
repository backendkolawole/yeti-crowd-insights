# Use-Case: 150 - Start the Event

## Goal

This use-case start the event selected by the client or it just starts all the event one-by one which should be started by default as the application starts.

## Pre-Conditions

- A list of events have been created the by client.

## Actors
- The client
- A scheduler

## Entry Points
- When a client selects an event to run
- When a scheduler starts the event

## Main Flow (Triggered by Client)
1. Client clicks on an event to run 
2. The Feed details are fetched by the system, for that event
    1. Run use-case [160 - Load Feed Configuration](160-Load_Feed_Configuration.md)
3. Each feed is run in a different thread.
    1. Run use-case [180 - Process the feed in real-time](180-Process_the_feed_real-time.md)
4. Return the running status of the feeds currently running for the event.  

## Secondary Flow (Triggered by Scheduler)
*TBD*

## Alternate Flow

## Exceptional Flow

## Implementation Details
### Class Description
- Create a class `StartEvent`. 
- It should have the following properties:
    - a function property `run_the_event` which accepts an `Event` object as parameter.
- `run_the_event` should call the `load_feeds` method of `Event` object to, load the feeds.
- Iteratively initialize `FeedProcessor` class and call its method `process_the_feed` for each feed of the event. Refer use-case [180 - Process the feed in real-time](180-Process_the_feed_real-time.md)


### Reference

