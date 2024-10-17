from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from config_app.models import Feed, FeedPolygon, Event, ZoneCount
from config_app.interface_adapters.serializers import FeedSerializer, FeedPolygonSerializer, EventSerializer, ClientSerializer, EventStatusSerializer, ZoneCountSerializer
from config_app.use_cases.client_use_case import ClientUseCase
from config_app.use_cases.event_use_case import EventUseCase
from config_app.use_cases.feed_use_case import FeedUseCase
from config_app.use_cases.feed_polygon_use_case import FeedPolygonUseCase
from config_app.use_cases.start_event_use_case import StartEventUseCase
from config_app.use_cases.event_status_use_case import EventStatusUseCase
from config_app.use_cases.zone_count_use_case import ZoneCountUseCase
from config_app.repositories.client_repository import ClientRepository
from config_app.repositories.event_repository import EventRepository
from config_app.repositories.feed_repository import FeedRepository
from config_app.repositories.feed_polygon_repository import FeedPolygonRepository
from config_app.repositories.start_event_repository import StartEventRepository
from config_app.repositories.event_status_repository import EventStatusRepository
from config_app.repositories.zone_count_repository import ZoneCountRepository
from config_app.models import Client, EventStatus
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied


class ClientList(generics.ListCreateAPIView):
    serializer_class = ClientSerializer

    queryset = Client.objects.all()
    repository = ClientRepository()
    use_case = ClientUseCase(ClientRepository())
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        return self.use_case.create_client(data=serializer.validated_data)

    def get_queryset(self):
        return self.use_case.get_all_clients()


class ClientDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer

    queryset = Client.objects.all()
    use_case = ClientUseCase(ClientRepository())
    permission_classes = [IsAdminUser]

    def get_object(self):
        client_id = self.kwargs['pk']
        return self.use_case.get_client(client_id=client_id)

    def perform_update(self, serializer):
        client_id = self.kwargs['pk']
        serializer.save()
        return self.use_case.update_client(
            client_id=client_id, data=serializer.validated_data)

    def perform_destroy(self, instance):
        return self.use_case.delete_client(client_id=instance.id)


class MyAccount(generics.ListAPIView):
    serializer_class = ClientSerializer

    queryset = Client.objects.all()
    use_case = ClientUseCase(ClientRepository())
    permission_classes = [IsAdminUser, IsAuthenticated]

    def get_object(self):
        client = self.request.user
        return self.use_case.get_client_account(client)

    # def perform_update(self, serializer):
    #     client_id = self.kwargs['pk']
    #     serializer.save()
    #     return self.use_case.update_client(
    #         client_id=client_id, data=serializer.validated_data)

    # def perform_destroy(self, instance):
    #     return self.use_case.delete_client(client_id=instance.id)


class EventList(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    use_case = EventUseCase(EventRepository())
    permission_classes = [IsAdminUser, IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return self.use_case.get_all_events(client=user)


class EventCreateView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    use_case = EventUseCase(EventRepository())
    permission_classes = [IsAdminUser, IsAuthenticated]

    def perform_create(self, serializer):

        user = self.request.user
        print(user)
        serializer.save(client=user)

        return self.use_case.create_event(client=user, data=serializer.validated_data)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    use_case = EventUseCase(EventRepository())
    permission_classes = [IsAdminUser, IsAuthenticated]

    def get_object(self):
        user = self.request.user
        event_id = self.kwargs['event_pk']
        return self.use_case.get_event(client=user, event_id=event_id)

    def perform_update(self, serializer):
        user = self.request.user
        event_id = self.kwargs['event_pk']

        return self.use_case.update_event(client=user, event_id=event_id, data=serializer.validated_data)

    def perform_delete(self, instance):
        user = self.request.user
        return self.use_case.delete_event(client=user, event_id=instance.event_id)


class StartEventView(generics.ListAPIView):
    use_case = StartEventUseCase(StartEventRepository())
    permission_classes = [IsAdminUser, IsAuthenticated]

    def get(self, request, event_pk, feed_pk):
        event_id = event_pk
        feed_id = feed_pk

        event_status_id = self.use_case.count_in_polygon(event_id, feed_id)

        return Response({"event_status_id": event_status_id}, status=status.HTTP_200_OK)


class EventStatusView(generics.ListAPIView):
    queryset = EventStatus.objects.all()
    serializer_class = EventStatusSerializer
    use_case = EventStatusUseCase(EventStatusRepository())
    permission_classes = [IsAdminUser, IsAuthenticated]

    def get(self, request):
        
        statuses = self.use_case.get_all_event_statuses()  # This should return a queryset
        serializer = self.serializer_class(
            statuses, many=True)  # Serialize the queryset
        # Return serialized data wrapped in a Response
        return Response(serializer.data)


class FeedList(generics.ListCreateAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    use_case = FeedUseCase(FeedRepository())

    permission_classes = [IsAdminUser, IsAuthenticated]

    def get_queryset(self):
        event_id = self.kwargs.get('event_pk')
        client = self.request.user

        return self.use_case.get_all_feed(client=client, event_id=event_id)

    def perform_create(self, serializer):
        event_id = self.kwargs.get('event_pk')
        client = self.request.user

        return self.use_case.create_feed(client=client, event_id=event_id, data=serializer.validated_data)


class FeedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    use_case = FeedUseCase(FeedRepository())

    def get_object(self):
        user = self.request.user

        event_id = self.kwargs.get('event_pk')
        feed_id = self.kwargs['feed_pk']
        return self.use_case.get_feed(client=user, event_id=event_id, feed_id=feed_id)

    def perform_update(self, serializer):
        event_id = self.kwargs.get('event_pk')
        client = self.request.user
        feed_id = self.kwargs['feed_pk']

        return self.use_case.update_feed(client=client, event_id=event_id, feed_id=feed_id, data=serializer.validated_data)

    def perform_destroy(self, instance):
        event_id = self.kwargs.get('event_pk')
        client = self.request.user
        return self.use_case.delete_feed(client=client, event_id=event_id, feed_id=instance.feed_id)


class FeedPolygonList(generics.ListCreateAPIView):
    serializer_class = FeedPolygonSerializer
    use_case = FeedPolygonUseCase(FeedPolygonRepository())
    queryset = FeedPolygon.objects.all()
    permission_classes = [IsAdminUser, IsAuthenticated]

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
        return self.use_case.get_feed_polygon(polygon_id=polygon_id, feed_id=feed_id, event_id=event_id)

    def perform_update(self, serializer):
        event_id = self.kwargs['event_pk']
        feed_id = self.kwargs['feed_pk']
        polygon_id = self.kwargs['pk']
        return self.use_case.update_feed_polygon(polygon_id=polygon_id, feed_id=feed_id, event_id=event_id, data=serializer.validated_data)

    def perform_destroy(self, instance):
        event_id = self.kwargs['event_pk']
        feed_id = self.kwargs['feed_pk']
        return self.use_case.delete_feed_polygon(polygon_id=instance.id, feed_id=feed_id, event_id=event_id)


class ZoneCount(generics.ListAPIView):
    queryset = ZoneCount.objects.all()
    serializer_class = ZoneCountSerializer
    use_case = ZoneCountUseCase(ZoneCountRepository())
    permission_classes = [IsAdminUser, IsAuthenticated]

    def get_queryset(self):
        
        zone_counts = self.use_case.get_all_zone_counts()  # This should return a queryset
        pass




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
