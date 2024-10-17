from config_app.repositories.feed_polygon_repository import FeedPolygonRepository


class FeedPolygonUseCase:
    def __init__(self, repository: FeedPolygonRepository):
        self.repository = repository

    def create_feed_polygon(self, feed_id, event_id, client, data):
        return self.repository.create_feed_polygon(feed_id=feed_id, event_id=event_id, client = client,  data=data)
    
    def get_all_feed_polygons(self, feed_id, event_id):
        return self.repository.get_all_feed_polygons(feed_id=feed_id, event_id=event_id)

    def get_feed_polygon(self, polygon_id, feed_id, event_id):
        return self.repository.get_feed_polygon(polygon_id=polygon_id, feed_id=feed_id, event_id=event_id)

    def update_feed_polygon(self, polygon_id, feed_id, event_id, data):
        return self.repository.update_feed_polygon(polygon_id=polygon_id, feed_id=feed_id, event_id=event_id, data=data)

    def delete_feed_polygon(self, polygon_id):
        return self.repository.delete_feed_polygon(polygon_id=polygon_id, feed_id=feed_id)