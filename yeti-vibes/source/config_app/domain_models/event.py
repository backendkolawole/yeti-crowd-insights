
class Event:
    def __init__(self, event_id, client, event_name, description, start_date, end_date, is_active):
        
        self.event_id = event_id
        self.client = client
        self.event_name = event_name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.is_active = is_active
        
    def __str__(self):
        return self.event_name
    
