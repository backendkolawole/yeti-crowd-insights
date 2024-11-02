class EventStatus:
    def __init__(self, event, status, timestamp):
        self.event = event
        self.status = status
        self.timestamp = timestamp
        
    def __str__(self):
        return self.status
