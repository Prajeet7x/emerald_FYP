from django.contrib import admin

# Register your models here.

from import_export.admin import ImportExportModelAdmin

from .models import *

admin.site.register(Club)
admin.site.register(Member)
admin.site.register(President)
admin.site.register(Event)
admin.site.register(EventParticipants)
admin.site.register(Feedback)
admin.site.register(Announcement)

class EventParticipantsAdmin(ImportExportModelAdmin):
    list_display = ('name', 'year', 'club', 'event')
