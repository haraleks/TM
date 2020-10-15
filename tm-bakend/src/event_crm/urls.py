from django.urls import path
from event_crm.views import (EventsView, EventsDetailView)


urlpatterns = [
        path('events/', EventsView.as_view(), name='events'),
        path('events/<int:pk>/', EventsDetailView.as_view(), name='events'),
]