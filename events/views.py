from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Event

# Create your views here.

def homePage(request):
    return HttpResponse('<h1>Welcome To... </h1>')


def listEventsStatic(request):
    list = [
        {
            'title': 'Event 1',
            'description': 'description 1',
        },
        {
            'title': 'Event 2',
            'description': 'description 2',
        },
        {
            'title': 'Event 3',
            'description': 'description 3',
        }
    ]
    return render(
        request,
        'events/listEvents.html',
        {
            'events': list,
        }
    )
    
    
def listEvents(request):
    list = Event.objects.all()
    #list = Event.objects.filter(state=True)
    return render(
        request,
        'events/listEvents.html',
        {
            'events': list,
        }
    )


def detailsEvent(request, id):
    event = Event.objects.get(id=id)
    return render(
        request,
        'events/event_detail.html',
        {
            'event': event,
        }
    )
    

def deleteEvent(request, id):
    Event.objects.get(id=id).delete()
    return redirect("events_list")