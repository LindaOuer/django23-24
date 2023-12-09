from django.urls import path
from .views import *

urlpatterns = [
    path('', homePage, name="Home_Page"),
    path('listStatic/', listEventsStatic, name="events_list_static"),
    path('list/', listEvents, name="events_list"),
    path('details/<int:id>', detailsEvent, name="events_details"),
    path('delete/<int:id>', deleteEvent, name="events_delete"),
]