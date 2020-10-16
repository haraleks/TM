from django.shortcuts import render
from django.views.generic.base import View

from event_crm.models import (Event, PartEvent)


class EventsView(View):
    """ Список мероприятий"""
    def get(self, request):
        events = Event.objects.first()
        return render(request, 'index.html', {'events_list': events})
        # return render(request, 'event/events_list.html', {'events_list': events})

class EventsDetailView(View):
    """ Список мероприятия"""
    def get(self, request, pk):
        event = Event.objects.get(pk=pk)
        part_events = PartEvent.objects.filter(event=event)
        return render(request, 'index.html', {'events_detail': event, 'part_events': part_events})


class PartEventsDetailView(View):
    """ Список мероприятия"""
    def get(self, request, pk):
        part_event = PartEvent.objects.get(pk=pk)
        return render(request, 'portfolio-detail/part_events.html', {'part_event': part_event})