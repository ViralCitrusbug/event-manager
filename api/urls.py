from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.EventList.as_view(),name='add-event'),
    path('/<pk>',views.EventCRUD.as_view(),name='event-crud'),
    path('/filter/<str:date>',views.EventFilter.as_view(),name='event-filter'),
    path('/filter/time/<pk>',views.EventOnTime.as_view(),name="event-on-time")
]
