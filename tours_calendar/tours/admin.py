from django.contrib import admin
from tours.models import Calendar, Tour



@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    list_display = ('calendar_name', 'get_tours')

    def get_tours(self, object):
        return ", ".join([i.name for i in object.tour_set.all()])


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'tour_length', 'color')




