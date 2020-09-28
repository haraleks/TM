from django.shortcuts import render
from django.views.generic.base import View

from event_crm.models import Event


class EventsView(View):
    """ Список мероприятий"""
    def get(self, request):
        events = Event.objects.all()
        return render(request, 'index.html', {'events_list': events})
        # return render(request, 'event/events_list.html', {'events_list': events})