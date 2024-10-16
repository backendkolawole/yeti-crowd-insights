from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


# Create your models here.

from django.contrib.auth.models import AbstractUser


class Client(AbstractUser):
    email = models.EmailField(unique=True)


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="events")
    event_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.event_name


class Feed(models.Model):
    feed_id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    feed_name = models.CharField(max_length=200)
    rtsp_link = models.URLField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.feed_name


class FeedPolygon(models.Model):
    polygon_id = models.AutoField(primary_key=True)
    feeds = models.ManyToManyField(Feed, related_name="feed_polygons")
    polygon_name = models.CharField(max_length=255)

    # Storing polygon as a list of tuples
    feed_polygons = ArrayField(
        ArrayField(models.IntegerField(), size=2),
        size=5
    )

    # Storing color as an array of integers
    polygon_color = ArrayField(models.IntegerField(), size=3)

    def __str__(self):
        return self.polygon_name


class EventStatus(models.Model):
    event_id = models.IntegerField()
    status = models.CharField(max_length=5)
    timestamp = models.DateTimeField(auto_now_add=True)
