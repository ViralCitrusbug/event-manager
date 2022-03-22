from asyncio import get_event_loop
from urllib import response
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from . serializer import *
from api import serializer
from .models import *
# Create your views here.

class EventList(APIView):
    def get(self,request):
        queryset = Event.objects.all()
        serializer = EventSerializer(queryset,many=True)
        return JsonResponse(serializer.data,safe=False)
    
    def post(self,request):
        serialize = EventSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return JsonResponse(serialize.data,safe=False)
        else: 
            return JsonResponse(serialize.errors,safe=False)
    
class EventCRUD(APIView):

    def get_event(self,pk):
        try:
            event = Event.objects.get(pk=pk)
            return event
        except Event.DoesNotExist:
            return False
    
    def get(self,request,pk):
        if self.get_event(pk):
            queryset = self.get_event(pk)
            serialize = EventSerializer(queryset)
            return JsonResponse(serialize.data,safe=False)
        else:
            return JsonResponse("Event Doesn't Exist")
    def put(self,request,pk):
        if self.get_event(pk):
            serializer = EventSerializer(self.get_event(pk),data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data,safe=False)
            else:
                return JsonResponse(serializer.errors)
        else:
            return JsonResponse("Event Doesn't Exist")

class EventFilter(APIView):
    def get(self,request,date):
        print(date)
        queryset = Event.objects.filter(date__date=date)
        serialize = EventSerializer(queryset,many=True)
        return JsonResponse(serialize.data,safe=False)

class EventOnTime(APIView):
    def get(self,request,pk):
        queryset = EventDate.objects.get(pk=pk)
        for i in queryset.event_set.all():
            print(i)
            print(i.eventtime_set.all())
        serializer = EventSerializer(queryset.event_set.all(),many=True)
        response = {
            'events':serializer.data
        }
        return JsonResponse(response,safe=False) 
  
