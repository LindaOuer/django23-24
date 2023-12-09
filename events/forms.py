from django import forms 
from datetime import date

from .models import * 
from users.models import Person

CATEGORY_CHOICES = (
        ('Music', 'Music'),
        ('Sport', 'Sport'),
        ('Cinema', 'Cinema'),
    )

class EventForm(forms.Form):
    title = forms.CharField(
        label= "Titre",
        max_length=150,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder': "Enter event title"
            }),
        )
    description = forms.CharField(label="Description", widget=forms.Textarea)
    eventImage = forms.ImageField(label="Image")
    category = forms.ChoiceField(label="Category", widget=forms.RadioSelect, choices=CATEGORY_CHOICES)
    nbrParticipants = forms.IntegerField(label="number of participants", min_value=0, step_size=1)
    eventDate = forms.DateField(
        label = "Event Date", 
        widget=forms.DateInput(
            attrs={
            'type': "date" }
        )
    )
    organizer = forms.ModelChoiceField(
        label= "Organizer",
        queryset=Person.objects.all()
    )
    

class EventFormModel(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        exclude = ['state']
    category = forms.ChoiceField(label="Category", widget=forms.RadioSelect, choices=CATEGORY_CHOICES)
    eventDate = forms.DateField(
        label = "Event Date",
        initial = date.today, 
        widget=forms.DateInput(
            attrs={
            'type': "date" }
        )
    )