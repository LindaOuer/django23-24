from django.urls import path
from .views import *

urlpatterns = [
    path('', homePage, name="Home_Page"),
    path('listStatic/', listEventsStatic, name="events_list_static"),
    path('list/', listEvents, name="events_list"),
    path('details/<int:id>', detailsEvent, name="events_details"),
    path('delete/<int:id>', deleteEvent, name="events_delete"),
    path('add/', addEvent, name="events_add"),
    path('listEvents/', EventsList.as_view(), name="events_listC"),
    path('eventsDetails/<int:pk>', EventsDetails.as_view(), name="events_DetailsC"),
    path('eventUpdate/<int:pk>', EventUpdateView.as_view(), name="events_UpdateC"),
    path('eventDelete/<int:pk>', EventDelete.as_view(), name="events_DeleteC"),
    path('participate/<int:id>', participateEvent, name="events_participate"),
]