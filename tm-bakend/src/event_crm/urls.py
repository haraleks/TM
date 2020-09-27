from django.urls import path
from event_crm.views import (EventView, PartEventsView, RegistrationEvent,
                             RegistrationEventView, EventParticipantsView, PaymentsView)

as_view_common = {
    'get': 'list',
    'post': 'create',
}

as_view_with_pk = {
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
}

urlpatterns = [
        path('events/', EventView.as_view(as_view_common), name='events'),
        path('events/<int:pk>/', EventView.as_view(as_view_with_pk), name='events_pk'),

        path('part_events/', PartEventsView.as_view(as_view_common), name='part_events'),
        path('part_events/<int:pk>/', PartEventsView.as_view(as_view_with_pk), name='part_events_pk'),

        path('reg_events/', RegistrationEventView.as_view(as_view_common), name='reg_events'),
        path('reg_events/<int:pk>/', RegistrationEventView.as_view(as_view_with_pk), name='reg_events_pk'),

        path('event_participants/', EventParticipantsView.as_view(as_view_common), name='event_participants'),
        path('event_participants/<int:pk>/', EventParticipantsView.as_view(as_view_with_pk), name='event_participants_pk'),

        path('payments/', PaymentsView.as_view(as_view_common), name='payments'),
        path('payments/<int:pk>/', PaymentsView.as_view(as_view_with_pk), name='payments'),

]