from django.urls import path
from event_crm.views import EventsView


urlpatterns = [
        path('events/', EventsView.as_view(), name='events'),
]