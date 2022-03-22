from rest_framework import serializers
from .models import *

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
    
    def create(self, validated_data):
        return Event.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        new_event = Event(**validated_data)
        new_event.id = instance.id
        new_event.save()
        return new_event

class EventDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventDate
        fields = "__all__"
    
    def create(self, validated_data):
        return EventDate(**validated_data)
    
    def update(self, instance, validated_data):
        new_event_date = EventDate(**validated_data)
        new_event_date.id = instance.id
        return new_event_date

class EventTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventTime
        fields = "__all__"
    
    def create(self, validated_data):
        return EventTime(**validated_data)
    
    def update(self, instance, validated_data):
        new_event_time = EventTime(**validated_data)
        new_event_time.id = instance.id
        return new_event_time