from django.contrib import admin
from .models import Feed, FeedPolygon, Event
# Register your models here.

admin.site.register(FeedPolygon)
admin.site.register(Feed)
admin.site.register(Event)
