from django.contrib import admin
from guide_p.models import Stations

# Register your models here.


@admin.register(Stations)
class StationAdmin(admin.ModelAdmin):
    pass