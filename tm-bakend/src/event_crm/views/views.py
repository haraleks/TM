from django.shortcuts import render
from django.views.generic.base import View
from django.utils import timezone

from event_crm.models import (Event, PartEvent)
from event_crm.constants import EventTypes


class EventsView(View):
    """ Список мероприятий"""
    def get(self, request):
        events = Event.objects.first()
        nlp_practic = PartEvent.objects.filter(event__type=EventTypes.NLP_PRAKTIC.value)

        return render(request, 'index.html', {'events_list': events, 'nlp_practics': nlp_practic})
        # return render(request, 'event/events_list.html', {'events_list': events})

class EventsDetailView(View):
    """ Список мероприятия"""
    def get(self, request, pk):
        event = Event.objects.get(pk=pk)
        part_events = PartEvent.objects.filter(event=event, start_at__gte=timezone.now()).order_by('pk')
        if part_events.count() > 1:
            part = part_events.first()
            name_part = part.name_part.name_plural + ':'
        elif part_events.count() == 1:
            part = part_events.first()
            name_part = part.name_part.name + ':'
        else:
            name_part = ''
        nlp_practic = PartEvent.objects.filter(event__type=EventTypes.NLP_PRAKTIC.value, start_at__gte=timezone.now())
        master_classes = Event.objects.filter(type=EventTypes.MASTER_CLASS.value, start_at__gte=timezone.now())
        return render(request, 'index.html', {'events_detail': event, 'part_events': part_events, 'nlp_practics': nlp_practic,
                                              'master_classes': master_classes, 'name_part': name_part})

class PartEventsDetailView(View):
    """ Список мероприятия"""
    def get(self, request, pk):
        part_event = PartEvent.objects.get(pk=pk)
        return render(request, 'blog-posts/blog-1.html', {'part_event': part_event})


class EventWithoutPart(View):
    def get(self, request, pk):
        event = Event.objects.get(pk=pk)
        return render(request, 'blog-posts/blog-1_1.html', {'event': event})

class NextEventView(View):
    """ Список мероприятия"""
    def get(self, request):
        ''' если дата мероприятия мерньше блока мероприятия, то выводим мероприятие, выводим ближайшую ступень'''
        date_now = timezone.now()
        event = Event.objects.filter(start_at__gte=date_now).order_by('start_at').last()
        part_event_first = PartEvent.objects.filter(start_at__gte=date_now).order_by('start_at').first()
        print("*"*20)
        print(event.start_at)
        print(part_event_first.start_at)
        print(event.start_at >= part_event_first.start_at)
        print("*" * 20)
        part_events = PartEvent.objects.filter(event=event, start_at__gte=timezone.now()).order_by('pk')
        nlp_practic = PartEvent.objects.filter(event__type=EventTypes.NLP_PRAKTIC.value, start_at__gte=timezone.now())
        master_classes = Event.objects.filter(type=EventTypes.MASTER_CLASS.value, start_at__gte=timezone.now())
        if part_event_first.start_at <= event.start_at:
            return render(request, 'index.html',
                          {'events_detail': part_event_first, 'part_events': "", 'nlp_practics': nlp_practic,
                           'master_classes': master_classes})
        return render(request, 'index.html', {'events_detail': event, 'part_events': part_events, 'nlp_practics': nlp_practic,
                                              'master_classes': master_classes})
