from django.contrib import admin
from .models import Event,EventDate,EventTime
# Register your models here.

class EventInline(admin.TabularInline):
    model = Event


class EventDateInline(admin.ModelAdmin):
    inlines = [EventInline]

admin.site.register(EventDate,EventDateInline)
admin.site.register(Event)
admin.site.register(EventTime)
