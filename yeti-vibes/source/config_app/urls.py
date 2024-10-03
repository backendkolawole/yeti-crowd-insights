from django.urls import path
from config_app.interface_adapters.views import ClientDetails, ClientList, EventDetail, EventList, FeedDetail, FeedList, FeedPolygonList, FeedPolygonDetails

urlpatterns = [
    path('', ClientList.as_view(), name='client-list'),
    path('<int:pk>/', ClientDetails.as_view(), name='client-detail'),
    path('events/', EventList.as_view(), name='event-list'),
    path('events/<int:event_pk>/', EventDetail.as_view(), name='event-detail'),
    path('events/<int:event_pk>/feed/', FeedList.as_view(), name="feed-list"),
    path('events/<int:event_pk>/feed/<int:feed_pk>/',
         FeedDetail.as_view(), name='feed-detail'),
    path('events/<int:event_pk>/feed/<int:feed_pk>/feed-polygon/',
         FeedPolygonList.as_view(), name='feed-polygon-list'),
    path('events/<int:event_pk>/feed/<int:feed_pk>/feed-polygon/<int:pk>/',
         FeedPolygonDetails.as_view(), name='feed-polygon-detail'),
]
