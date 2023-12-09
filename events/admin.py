from django.contrib import admin
from .models import Event

# Register your models here.

class ParticipantsFilter(admin.SimpleListFilter):
    title = 'Participants'
    parameter_name = 'nbrParticipants'
    
    def lookups (self, request, model_admin):
        return (
            ('0', 'No Participants'),
            ('more', 'There are participants')
        )
        
    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.filter(nbrParticipants__exact=0)
        else:
            return queryset.filter(nbrParticipants__gte=1)
            
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'state'
    )
    
    ordering = (
        '-title',
        '-updated_at'
    )
    
    search_fields = [
        'title', 'category'
    ]
    
    list_per_page = 3
    
    readonly_fields = ('created_at', 'updated_at')
    
    list_filter = ('state', 'category', ParticipantsFilter)
    
    fieldsets = (
        (
            'state', 
            {
                'fields': ('state',)
            }
        ),
        (
            'About', {
                'classes': ('collapse',),
                'fields': (
                    'title',
                    'category',
                    'eventImage',
                    "nbrParticipants",
                    'description',
                    'organizer'
                )
            }
        ),
        (
            'Dates',
            {
                'fields': ('eventDate', 'created_at', 'updated_at')
            }
        )
    )

admin.site.register(Event, EventAdmin)