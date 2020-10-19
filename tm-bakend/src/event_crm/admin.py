from django.contrib import admin
from event_crm.models import (Event, PartEvent, RegistrationEvent,
                              EventParticipant, Payments, NamePart)


admin.site.register(Event)
admin.site.register(NamePart)
admin.site.register(PartEvent)
admin.site.register(RegistrationEvent)
admin.site.register(EventParticipant)
admin.site.register(Payments)
