from django.contrib import admin
from event_crm.models import (Event, PartEvent, RegistrationEvent,
                              EventParticipant, Payments)


admin.site.register(Event)
admin.site.register(PartEvent)
admin.site.register(RegistrationEvent)
admin.site.register(EventParticipant)
admin.site.register(Payments)
