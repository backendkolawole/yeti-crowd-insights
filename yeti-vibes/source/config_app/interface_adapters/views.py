from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from config_app.models import Feed, FeedPolygon, Event
from config_app.interface_adapters.serializers import FeedSerializer, FeedPolygonSerializer, EventSerializer, ClientSerializer
from config_app.use_cases.client_use_case import ClientUseCase
from config_app.use_cases.event_use_case import EventUseCase
from config_app.use_cases.feed_use_case import FeedUseCase
from config_app.use_cases.feed_polygon_use_case import FeedPolygonUseCase
from config_app.repositories.client_repository import ClientRepository
from config_app.repositories.event_repository import EventRepository
from config_app.repositories.feed_repository import FeedRepository
from config_app.repositories.feed_polygon_repository import FeedPolygonRepository
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated




class ClientList(generics.ListCreateAPIView):
    serializer_class = ClientSerializer
    
    queryset = User.objects.all()
    repository = ClientRepository()
    use_case = ClientUseCase(ClientRepository())
    

    # permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        return self.use_case.create_client(data = serializer.validated_data)
    
    def get_queryset(self):
        return self.use_case.get_all_clients()
       
        

class ClientDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer
    
    queryset = User.objects.all()
    use_case = ClientUseCase(ClientRepository())
    # permission_classes = [IsAdminUser]
    
    def get_object(self):
        client_id = self.kwargs['pk']
        return self.use_case.get_client(client_id=client_id)
    
    def perform_update(self, serializer):
        client_id = self.kwargs['pk']


        # return self.use_case.update_client(client_id=client_id, data = serializer.validated_data)
        return self.use_case.update_client(
            client_id=client_id, data=serializer.validated_data)
        # print(f"Updated client: {client}, Type: {type(client)}")
        # Serializing the updated client if needed
        # return self.use_case.perform_update(client_id = client_id, data = serializer.validated_data)
    
        
    def perform_destroy(self, instance):
        return self.use_case.delete_client(client_id=instance.id)
    


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    use_case = EventUseCase(EventRepository())
    # permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        user = self.request.user if self.request.user.is_authenticated else None
        return self.use_case.create_event(client=user, data=serializer.validated_data)

    def get_queryset(self):
        user = self.request.user
        return self.use_case.get_all_events(client=user)
    
    

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    use_case = EventUseCase(EventRepository())
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        event_id = self.kwargs['event_pk']
        return self.use_case.get_event(client = user, event_id = event_id)
    
    def perform_update(self, serializer):
        user = self.request.user
        event_id = self.kwargs['event_pk']
        
        return self.use_case.update_event(client = user, event_id = event_id, data = serializer.validated_data)
    
    def perform_delete(self, client):
        user = self.request.user
        event_id = self.kwargs['event_pk']
        return self.use_case.delete_event(client=user, event_id = event_id)
    

    
class FeedList(generics.ListCreateAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    use_case = FeedUseCase(FeedRepository())

    # permission_classes = [IsAdminUser]


    def get_queryset(self):
        event_id = self.kwargs.get('event_pk') 
        client = self.request.user

        return self.use_case.get_all_feed(client=client, event_id=event_id)
        
    def perform_create(self, serializer):
        event_id = self.kwargs.get('event_pk')
        client = self.request.user

        return self.use_case.create_feed(client=client, event_id=event_id, data = serializer.validated_data)    
    
    
class FeedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    # permission_classes = [IsAdminUser]
    use_case = FeedUseCase(FeedRepository())

    
    def get_object(self):
        event_id = self.kwargs.get('event_pk')
        client = self.request.user
        feed_id = self.kwargs['feed_pk']
        return self.use_case.get_feed(client = client, event_id=event_id, feed_id=feed_id)

    def perform_update(self, serializer):
        event_id = self.kwargs.get('event_pk')
        client = self.request.user
        feed_id = self.kwargs['feed_pk']
        return self.use_case.update_feed(client = client, event_id=event_id, feed_id=feed_id, data = serializer.validated_data)

    def perform_destroy(self, instance):
        event_id = self.kwargs.get('event_pk')
        client = self.request.user
        return self.use_case.delete_feed(client = client, event_id=event_id, feed_id=instance.id)

    
class FeedPolygonList(generics.ListCreateAPIView):
    serializer_class = FeedPolygonSerializer
    use_case = FeedPolygonUseCase(FeedPolygonRepository())
    queryset = FeedPolygon.objects.all()

    def perform_create(self, serializer):
        event_id = self.kwargs['event_pk']
        feed_id = self.kwargs['feed_pk']
        return self.use_case.create_feed_polygon(feed_id=feed_id, event_id=event_id, data=serializer.validated_data)
    
    def get_queryset(self):
        event_id = self.kwargs['event_pk']
        feed_id = self.kwargs['feed_pk']
        return self.use_case.get_all_feed_polygons(feed_id=feed_id, event_id=event_id)



class FeedPolygonDetails(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = FeedPolygonSerializer
    use_case = FeedPolygonUseCase(FeedPolygonRepository())

    def get_object(self):
        event_id = self.kwargs['event_pk']
        feed_id = self.kwargs['feed_pk']
        polygon_id = self.kwargs['pk']
        return self.use_case.get_feed_polygon(polygon_id = polygon_id, feed_id = feed_id, event_id = event_id)

    def perform_update(self, serializer):
        event_id = self.kwargs['event_pk']
        feed_id = self.kwargs['feed_pk']
        polygon_id = self.kwargs['pk']
        return self.use_case.update_feed_polygon(polygon_id = polygon_id, feed_id = feed_id, event_id= event_id, data = serializer.validated_data)

    def perform_destroy(self, instance):
        event_id = self.kwargs['event_pk']
        feed_id = self.kwargs['feed_pk']
        return self.use_case.delete_feed_polygon(polygon_id=instance.id, feed_id = feed_id, event_id = event_id)







# from django.contrib.auth.models import User
# # from config_app.serializers import 
# from rest_framework import generics
# from rest_framework.permissions import IsAdminUser
# from .models import Feed, FeedPolygon, Event, Client
# from .serializers import FeedSerializer, FeedPolygonSerializer, EventSerializer, ClientSerializer
# from rest_framework.exceptions import NotFound



# class ClientList(generics.ListCreateAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer
#     # permission_classes = [IsAdminUser]


# class ClientDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer
#     # permission_classes = [IsAdminUser]
    

# class EventList(generics.ListCreateAPIView):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer
#     # permission_classes = [IsAdminUser]
    
#     # def get_queryset(self):
#     #     pk = self.kwargs.get('pk')
#     #     customer = Client.objects.get(pk=pk)
#     #     return Event.objects.get(customer=customer)
    

#     def get_queryset(self):
#         try:
#             customer = Client.objects.get(pk=self.kwargs['pk'])
#         except Client.DoesNotExist:
#             raise NotFound("Client not found.")
#         return Event.objects.get(customer=customer)

    

# class EventDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer
#     # permission_classes = [IsAdminUser]
    
    

    
# class FeedList(generics.ListCreateAPIView):
#     queryset = Feed.objects.all()
#     serializer_class = FeedSerializer
#     # permission_classes = [IsAdminUser]
    
    
#     # def get_queryset(self):
#     #     pk = self.kwargs.get('pk')
#     #     event = Event.objects.get(pk=pk)
#     #     return Feed.objects.filter(feed_event=event)
    
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')  # Adjust this based on how you're retrieving the ID
#         try:
#             event = Event.objects.get(pk=pk)
#         except Event.DoesNotExist:
#             raise NotFound("Event matching query does not exist.")
#         return Feed.objects.get(feed_event=event)
        
#     def perform_create(self, serializer):
#         pk = self.kwargs.get('pk')
#         event = Event.objects.get(pk=pk)
#         serializer.save(feed_event=event)
    
    
# class FeedDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Feed.objects.all()
#     serializer_class = FeedSerializer
#     # permission_classes = [IsAdminUser]
    
    
    
# class FeedPolygonList(generics.ListCreateAPIView):
    
#     def get_queryset(self):
#         """
#         This view should return a list of all the purchases for
#         the user as determined by the username portion of the URL.
#         """
#         pk = self.kwargs.get('pk')
#         return FeedPolygon.objects.filter(feed_id=pk)
    

# class FeedPolygonDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = FeedPolygon.objects.all()
#     serializer_class = FeedPolygonSerializer
#     # permission_classes = [IsAdminUser]
    



