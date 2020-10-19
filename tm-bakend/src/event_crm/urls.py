from django.urls import path
from event_crm.views import (EventsView, EventsDetailView, PartEventsDetailView, EventWithoutPart,
                             NextEventView)


urlpatterns = [
        path('', NextEventView.as_view(), name='next_event'),
        path('events/', EventsView.as_view(), name='events'),
        path('events/<int:pk>/', EventsDetailView.as_view(), name='events_pk'),
        path('event_without_part/<int:pk>/', EventWithoutPart.as_view(), name='event_without_part'),

        path('part_events/<int:pk>/', PartEventsDetailView.as_view(), name='part_events_pk'),
]