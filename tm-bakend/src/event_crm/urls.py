from django.urls import path
from event_crm.views import (EventsView, EventsDetailView, PartEventsDetailView)


urlpatterns = [
        path('events/', EventsView.as_view(), name='events'),
        path('events/<int:pk>/', EventsDetailView.as_view(), name='events_pk'),

        path('part_events/<int:pk>/', PartEventsDetailView.as_view(), name='part_events_pk'),
]