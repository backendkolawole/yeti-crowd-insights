from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from config_app.models import Feed, FeedPolygon, Event, ZoneCount, Client, EventStatus, FeedStatus
from config_app.interface_adapters.serializers import FeedSerializer, FeedPolygonSerializer, EventSerializer, EventCreateSerializer,  ClientSerializer, EventStatusSerializer, FeedStatusSerializer, ZoneCountSerializer, FeedDetailSerializer, LoginSerializer
from config_app.use_cases.client_use_case import ClientUseCase
from config_app.use_cases.event_use_case import EventUseCase
from config_app.use_cases.feed_use_case import FeedUseCase
from config_app.use_cases.feed_polygon_use_case import FeedPolygonUseCase
from config_app.use_cases.zone_count_use_case import ZoneCountUseCase
from config_app.repositories.client_repository import ClientRepository
from config_app.repositories.event_repository import EventRepository
from config_app.repositories.feed_repository import FeedRepository
from config_app.repositories.feed_polygon_repository import FeedPolygonRepository
from config_app.repositories.zone_count_repository import ZoneCountRepository
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import threading
from yolov8_region_counter import stop_feed
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


class ClientList(generics.ListCreateAPIView):
    serializer_class = ClientSerializer

    queryset = Client.objects.all()
    repository = ClientRepository()
    use_case = ClientUseCase(ClientRepository())

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


@swagger_auto_schema(tags=['Events'])
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
    serializer_class = EventCreateSerializer
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


@swagger_auto_schema(
    operation_summary="Retrieve a feed",
    tags=['Feed']
)
class FeedList(generics.ListCreateAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    use_case = FeedUseCase(FeedRepository())

    permission_classes = [IsAdminUser, IsAuthenticated]

    @swagger_auto_schema(tags=['Feed'])
    def get_queryset(self):
        event_id = self.kwargs.get('event_pk')
        client = self.request.user

        return self.use_case.get_all_feed(client=client, event_id=event_id)

    @swagger_auto_schema(tags=['Feed'])
    def perform_create(self, serializer):
        event_id = self.kwargs.get('event_pk')
        client = self.request.user

        return self.use_case.create_feed(client=client, event_id=event_id, data=serializer.validated_data)


class FeedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedDetailSerializer
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
        client = self.request.user

        event_id = self.kwargs['event_pk']
        feed_id = self.kwargs['feed_pk']
        return self.use_case.create_feed_polygon(feed_id=feed_id, event_id=event_id, client=client, data=serializer.validated_data)

    def get_queryset(self):
        event_id = self.kwargs['event_pk']
        feed_id = self.kwargs['feed_pk']
        return self.use_case.get_all_feed_polygons(feed_id=feed_id, event_id=event_id)


class FeedPolygonDetails(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = FeedPolygonSerializer
    use_case = FeedPolygonUseCase(FeedPolygonRepository())
    permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = FeedPolygon.objects.all()

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


class StartFeedView(generics.CreateAPIView):
    queryset = FeedStatus.objects.all()
    serializer_class = FeedStatusSerializer
    use_case = FeedUseCase(FeedRepository())
    permission_classes = [IsAdminUser, IsAuthenticated]

    def post(self, request, event_pk, feed_pk):
        user = self.request.user
        event_id = event_pk
        feed_id = feed_pk

        feed_status = self.use_case.start_the_feed(
            client=user, event_id=event_id, feed_id=feed_id)

        serializer = self.get_serializer(feed_status)
        return Response(serializer.data, status=status.HTTP_200_OK)

        # self.use_case.start_the_feed(
        #     client=user, event_id=event_id, feed_id=feed_id)

        # return Response({"message": "Video feed started"}, status=status.HTTP_200_OK)


class StopFeedView(generics.DestroyAPIView):
    queryset = FeedStatus.objects.all()
    serializer_class = FeedStatusSerializer
    use_case = FeedUseCase(FeedRepository())
    permission_classes = [IsAdminUser, IsAuthenticated]

    def post(self, request, *args, **kwargs):
        global stop_feed
        stop_feed = True
        print("Stop feed request received, stop_feed set to True.", stop_feed)

        user = self.request.user
        event_id = self.kwargs["event_pk"]
        feed_id = self.kwargs["feed_pk"]

        feed_status = self.use_case.stop_the_feed(
            client=user, event_id=event_id, feed_id=feed_id)

        serializer = self.get_serializer(feed_status)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FeedStatusView(generics.ListAPIView):
    queryset = FeedStatus.objects.all()
    serializer_class = FeedStatusSerializer
    use_case = FeedUseCase(FeedRepository())
    permission_classes = [IsAdminUser, IsAuthenticated]

    def get(self, request):

        statuses = self.use_case.get_all_feed_statuses()  # This should return a queryset
        serializer = self.serializer_class(
            statuses, many=True)  # Serialize the queryset
        # Return serialized data wrapped in a Response
        return Response(serializer.data)


class ZoneCount(generics.ListAPIView):
    queryset = ZoneCount.objects.all()
    serializer_class = ZoneCountSerializer
    use_case = ZoneCountUseCase(ZoneCountRepository())
    permission_classes = [IsAdminUser, IsAuthenticated]

    # def perform_create(self, serializer):

    #     user = self.request.user
    #     print(user)
    #     serializer.save(client=user)

    #     return self.use_case.create_event(client=user, data=serializer.validated_data)

    def get_queryset(self):

        zone_counts = self.use_case.get_all_zone_counts()  # This should return a queryset
        pass



class CustomLoginView(APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        # print(request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            print(username, password)
            user = authenticate(request, username=username, password=password)
            print(f'user: {user}')

            if user is not None:
                login(request, user)
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomLogoutView(APIView):

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)



def logout_view(request):
    print(request.method)
    if request.method == 'POST':
        logout(request)
        # Redirect to the desired URL after logout
        return HttpResponseRedirect(reverse('http://127.0.0.1:8000/swagger'))
    elif request.method == 'GET':
        logout(request)

        # If the request includes a 'next' parameter, use that
        if 'next' in request.GET:
            redirect_url = request.GET['next']
        else:
            # Otherwise, use the default URL
            redirect_url = reverse('http://127.0.0.1:8000/swagger')
        # Redirect the user to the specified URL after logout
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponse(status=405)



# class StartEventView(generics.ListAPIView):
#     queryset = EventStatus.objects.all()
#     serializer_class = EventStatusSerializer
#     use_case = EventUseCase(EventRepository())
#     permission_classes = [IsAdminUser, IsAuthenticated]

#     def get(self, request, event_pk, feed_pk):
#         user = self.request.user
#         event_id = event_pk
#         feed_id = feed_pk

#         # Call the use case to start the event
#         event_status = self.use_case.start_the_event(
#             client=user, event_id=event_id, feed_id=feed_id)

#         # Serialize the event status before returning it
#         serializer = self.get_serializer(event_status)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# class StopEventView(generics.ListAPIView):
#     queryset = EventStatus.objects.all()
#     serializer_class = EventStatusSerializer
#     use_case = EventUseCase(EventRepository())
#     permission_classes = [IsAdminUser, IsAuthenticated]

#     def get(self, request, event_pk, feed_pk):
#         event_id = event_pk
#         feed_id = feed_pk

#         event_status_id = self.use_case.stop_the_event(event_id, feed_id)

#         return Response({"event_status_id": event_status_id}, status=status.HTTP_200_OK)


# class EventStatusView(generics.ListAPIView):
#     queryset = EventStatus.objects.all()
#     serializer_class = EventStatusSerializer
#     use_case = EventStatusUseCase(EventStatusRepository())
#     permission_classes = [IsAdminUser, IsAuthenticated]

#     def get(self, request):

#         statuses = self.use_case.get_all_event_statuses()  # This should return a queryset
#         serializer = self.serializer_class(
#             statuses, many=True)  # Serialize the queryset
#         # Return serialized data wrapped in a Response
#         return Response(serializer.data)


# class GoogleLogin(APIView):
#     permission_classes = (AllowAny,)

#     def get(self, request, *args, **kwargs):
#         # Redirect to Google OAuth2 login
#         return Response({"url": "your_google_auth_url_here"})

# Add this view to your urls.py
#

# class CustomLoginView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return JsonResponse({'message': 'Login successful'}, status=status.HTTP_200_OK)
#         else:
#             return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)