class EventStatus:
    def __init__(self, event_id, status, timestamp):
        self.event_id = event_id
        self.status = status
        self.timestamp = timestamp
        
    def __str__(self):
        return self.status
