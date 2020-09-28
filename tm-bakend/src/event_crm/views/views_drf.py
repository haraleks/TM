from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from event_crm.models import (Event, PartEvent, EventParticipant,
                              Payments, RegistrationEvent)
from event_crm.serializers import (ViewEventSerializer, ViewPartEventsSerializer,
                                   ViewRegistrationEventSerializer, ViewEventParticipantsSerializer,
                                   ViewPaymentsSerializer)


class EventView(ModelViewSet):
    serializer_class = ViewEventSerializer
    queryset = Event.objects.all()


class PartEventsView(ModelViewSet):
    serializer_class = ViewPartEventsSerializer
    queryset = PartEvent.objects.all()


class RegistrationEventView(ModelViewSet):
    serializer_class = ViewRegistrationEventSerializer
    queryset = RegistrationEvent.objects.all()


class EventParticipantsView(ModelViewSet):
    serializer_class = ViewEventParticipantsSerializer
    queryset = EventParticipant.objects.all()


class PaymentsView(ModelViewSet):
    serializer_class = ViewPaymentsSerializer
    queryset = Payments.objects.all()