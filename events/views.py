from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from .models import Event, Participation
from .forms import EventForm,EventFormModel

from users.models import Person

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


def addEvent(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            Event.objects.create(**form.cleaned_data)
            return redirect('events_list')
        
    return render(request, "events/event_add.html",
                {'form': form})
    
def addEventModel(request):
    form = EventFormModel()
    if request.method == "POST":
        form = EventFormModel(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('events_list')
        
    return render(request, "events/event_add.html",
                {'form': form})
    

def participateEvent(request, id):
    event = Event.objects.get(id=id)
    person = Person.objects.get(CIN='12345679')
    # person = request.user

    if Participation.objects.filter(person=person, event=event).count() == 0:
        Participation.objects.create(person=person, event=event)

        event.nbrParticipants += 1
        event.save()

        # nb = event.nbrParticipants + 1
        # Event.objects.filter(id=id).update(nbrParticipants=nb)

    return redirect("events_list")


class EventCreateView(CreateView):
    model = Event
    form_class = EventFormModel 
    success_url = reverse_lazy('events_list')
    template_name = "events/event_add.html"

class EventUpdateView(UpdateView):
    model = Event
    form_class = EventFormModel 
    success_url = reverse_lazy('events_list')
    template_name = "events/event_add.html"

class EventsList(ListView):
    model = Event
    template_name = 'events/listEvents.html'
    context_object_name = 'events'
    #queryset = Event.objects.filter(state=True)
    
class EventsDetails(DetailView):
    model = Event
    

class EventDelete(DeleteView):
    model = Event
    success_url = reverse_lazy('events_list')