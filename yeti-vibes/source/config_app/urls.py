from django.urls import path
from .views import ClientDetails, ClientList, EventDetail, EventList, FeedDetail, FeedList, FeedPolygonList, FeedPolygonDetails

urlpatterns = [
    path('clients/<int:pk>/', ClientDetails.as_view(), name='client-detail'),
    path('clients/', ClientList.as_view(), name='client-list'),
    path('events/<int:pk>/', EventDetail.as_view(), name='event-detail'),
    path('events/', EventList.as_view(), name='event-list'),
    path('feed/<int:pk>/', FeedDetail.as_view(), name='feed-detail'),
    path('feed/', FeedList.as_view(), name="feed-list"),
    path('feed-polygon/', FeedPolygonList.as_view(), name='feed-polygon-list'),
    path('feed-polygon/<int:pk>/', FeedPolygonDetails.as_view(), name='feed-polygon-detail'),
]
