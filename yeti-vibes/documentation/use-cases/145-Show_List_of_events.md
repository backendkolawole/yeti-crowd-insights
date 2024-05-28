# Use-Case: 145 - Show List of events

## Goal

Shows a list of events for a client on a UI

## Pre-Conditions

- An end-point exists to fetch the list of events

## Actors

- The client

## Entry Points

- Is triggered when client navigates to their events page

## Main Flow

1. Client navigates to the Events-List page
2. The page calls the service end-point, to get the list of events, by providing it with the client id.
3. The system sends back the list of events for that client

## Alternate Flow

## Exceptional Flow

## Implementation Details

### Data Source for Events

#### Json file (POC implementation)

- Define a json file `event_config.json`
- it should have the following fields
  - Client Id (integer)
  - Event id (integer)
  - Event name (string)
  - Event description (string)
  - start date/time (date-time)
    - not defined, if the event should start as soon as the app is started
  - end date/time (date-time)
    - not defined, if the event is never ending
- isActive flag as boolean.


### Class Description

#### `EventLoader` Class

- This class loads Events for a given client Id.
- It has a method `load_events` which takes a client Id as parameter.
- The method returns an array of objects of `Event` type for that client id.

#### `Event` Class

- this class holds the details of an event of the client
- This class has following properties:
  - ClientId as integer
  - EventId as integer
  - EventName as integer
  - EventDescription as string
  - StartDate as DateTime
  - EndDate as DateTime
  - IsActive as boolean. (this flag decides if the event should be run or not)
  - Array of `Feed` objects
- Create a function `get_feeds` which uses `self.EvenId` as parameter.
    - this function loads the feeds from the data source and fills the `Feed` objects, defined in use case [Use-Case: 160 - Load Feed Configuration](160-Load_Feed_Configuration.md), to load feeds for this event.
