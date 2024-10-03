    
class Feed:
    
    def __init__(self, feed_id, event, feed_name, rtsp_link, is_active):
        self.feed_id =  feed_id
        self.event = event
        self.feed_name  = feed_name
        self.rtsp_link  = rtsp_link
        self.is_active  = is_active
        
    def __str__(self):
        return self.feed_name
