from django.urls import path
from config_app.interface_adapters.views import ClientDetails, ClientList, EventDetail, EventList, EventCreateView, FeedDetail, FeedList, FeedPolygonList, FeedPolygonDetails, MyAccount, StartFeedView, StopFeedView, FeedStatusView, CustomLoginView, CustomLogoutView, logout_view

urlpatterns = [
    path('accounts', ClientList.as_view(), name='client-list'),
    path('accounts/<int:pk>/', ClientDetails.as_view(), name='client-detail'),
    path('events/', EventList.as_view(), name='event-list'),
    path('events/create/', EventCreateView.as_view(), name='event-create'),
    path('events/<int:event_pk>/', EventDetail.as_view(), name='event-detail'),
    path('events/<int:event_pk>/feed/', FeedList.as_view(), name="feed-list"),
    path('events/<int:event_pk>/feed/<int:feed_pk>/',
         FeedDetail.as_view(), name='feed-detail'),
    path('events/<int:event_pk>/feed/<int:feed_pk>/feed-polygons/',
         FeedPolygonList.as_view(), name='feed-polygon-list'),
    path('events/<int:event_pk>/feed/<int:feed_pk>/feed-polygons/<int:pk>/',
         FeedPolygonDetails.as_view(), name='feed-polygon-detail'),
    path('events/<int:event_pk>/feed/<int:feed_pk>/start/',
         StartFeedView.as_view(), name='start-feed'),
    path('events/<int:event_pk>/feed/<int:feed_pk>/stop/',
         StopFeedView.as_view(), name='stop-feed'),
    path('events/<int:event_pk>/feed/status/',
         FeedStatusView.as_view(), name='feed-status'),
    path('api/login/', CustomLoginView.as_view(), name='api-login'),
    path('api/logout/', CustomLogoutView.as_view(), name='api-logout'),
    path('accounts/logout/', logout_view, name='logout'),
#     path('accounts/login/', login_view, name='login'),


    #     path('events/<int:event_pk>/feed/<int:feed_pk>/start/',
    #          StartEventView.as_view(), name='start-event'),
    # path('events/<int:event_pk>/feed/<int:feed_pk>/stop/',
    #     StopEventView.as_view(), name='stop-event'),
    #     path('events/status/',
    #          EventStatusView.as_view(), name='event-status'),
    path("profile", MyAccount.as_view(), name="feed_list")
]
