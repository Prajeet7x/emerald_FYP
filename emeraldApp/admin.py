from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Club)
admin.site.register(Member)
admin.site.register(President)
admin.site.register(Event)
