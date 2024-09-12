from django.contrib import admin
from .models import Feed, FeedPolygon, Event, Client
# Register your models here.

admin.site.register(Client)
admin.site.register(FeedPolygon)
admin.site.register(Feed)
admin.site.register(Event)
