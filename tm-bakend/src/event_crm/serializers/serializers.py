from rest_framework import serializers
from event_crm.models import (Event, EventParticipant, PartEvent,
                              Payments, RegistrationEvent)


class ViewEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'


class ViewPartEventsSerializer(serializers.ModelSerializer):

    class Meta:
        model = PartEvent
        fields = '__all__'


class ViewRegistrationEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegistrationEvent
        fields = '__all__'


class ViewEventParticipantsSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventParticipant
        fields = '__all__'


class ViewPaymentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = '__all__'
