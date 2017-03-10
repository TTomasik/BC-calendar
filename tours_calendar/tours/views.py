from django.shortcuts import render, redirect
from django.views import View
from calendar import monthrange
import datetime
from django.views.generic import DeleteView, UpdateView
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from tours.forms import TourForm
from tours.models import Tour, Calendar


class TourInfo(View):
    def get(self, request, tour_id):
        cont = {}
        calendar = Calendar.objects.filter(tour__id=tour_id)[0].calendar_name
        tour = Tour.objects.get(id=tour_id)
        cont['name'] = tour.name
        cont['destination'] = tour.destination
        cont['start_date'] = tour.start_date
        cont['end_date'] = tour.end_date
        cont['first_name'] = tour.first_name
        cont['last_name'] = tour.last_name
        cont['company'] = tour.company
        cont['phone'] = tour.phone
        cont['date_of_entry'] = tour.date_of_entry
        cont['color'] = tour.color
        cont['length'] = tour.tour_length
        cont['calendar'] = calendar
        cont['null'] = ['']
        return render(request, "tours/tour_info.html", cont)


class CalendarInfo(View):
    def get(self, request, calendar_id):
        cont = {}
        tour_list = []
        cal = Calendar.objects.get(id=calendar_id)
        tours = cal.tour_set.all()

        for tour in tours:
            d = {}
            d['tour_name'] = tour.name
            d['start_date'] = tour.start_date
            d['end_date'] = tour.end_date
            d['color'] = tour.color
            d['tour_id'] = tour.id
            tour_list.append(d)
        cont['tour_list'] = tour_list
        cont['name'] = cal.calendar_name
        return render(request, "tours/calendar.html", cont)


class AddTour(View):
    def get(self, request):
        form = TourForm()
        return render(request, "tours/add_tour.html", {"form": form})

    def post(self, request):
        form = TourForm(request.POST)
        if form.is_valid():
            tour_name = form.cleaned_data['name']
            tour_destination = form.cleaned_data['destination']
            tour_start_date = form.cleaned_data['start_date']
            tour_end_date = form.cleaned_data['end_date']
            if tour_end_date == None:
                year = int(str(tour_start_date)[0:4])
                month = int(str(tour_start_date)[5:7])
                last_day = monthrange(year, month)[1]
                tour_end_date = datetime.date(year, month, last_day)
            tour_first_name = form.cleaned_data['first_name']
            tour_last_name = form.cleaned_data['last_name']
            tour_company = form.cleaned_data['company']
            tour_phone = form.cleaned_data['phone']
            tour_color = form.cleaned_data['color']
            tour_calendar_name = form.cleaned_data['tour_calendar']
            tour = Tour.objects.create(
                name = tour_name,
                destination = tour_destination,
                start_date = tour_start_date,
                end_date = tour_end_date,
                first_name = tour_first_name,
                last_name = tour_last_name,
                company = tour_company,
                phone = tour_phone,
                color = tour_color,
                tour_calendar = tour_calendar_name
            )
            tour.save()
            calendar_id = Calendar.objects.get(calendar_name=tour_calendar_name).id
        return redirect("/calendar/{}".format(calendar_id))


class DeleteTour(DeleteView):
    def get_success_url(self, **kwargs):
        return reverse('calendar', kwargs={'calendar_id':Calendar.objects.filter(tour__id=self.object.id)[0].id})
    model = Tour
    fields = '__all__'
    template_name_suffix = '_delete_form'


class EditTour(View):
    def get(self, request, tour_id):
        tour = Tour.objects.get(id=tour_id)
        form = TourForm(instance=tour)
        return render(request, "tours/add_tour.html", {"form": form})

    def post(self, request, tour_id):
        tour = Tour.objects.get(id=tour_id)
        form = TourForm(request.POST, instance=tour)
        if form.is_valid():
            if form.cleaned_data['end_date'] == None:
                tour_start_date = form.cleaned_data['start_date']
                year = int(str(tour_start_date)[0:4])
                month = int(str(tour_start_date)[5:7])
                last_day = monthrange(year, month)[1]
                tour.end_date = datetime.date(year, month, last_day)
                tour.save()
            form.save()
        calendar_id = Calendar.objects.filter(tour__id=tour_id)[0].id
        return redirect("/calendar/{}".format(calendar_id))


class Index(View):
    def get(self, request):
        cont = {}
        cont['calendars'] = Calendar.objects.all()
        return render(request, "tours/index.html", cont)







