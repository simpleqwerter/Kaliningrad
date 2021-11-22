from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect, HttpResponseNotFound
from guide_p.forms import StationForm
from guide_p.models import Stations
from helpers.db_init import csv_dict_reader


# Create your views here.


class Redirect(View):

    def get(self, request):
        return HttpResponseRedirect('/api/data')


class GuideHome(View):
    some = None
    if Stations.objects.first() is not None:
        some = Stations.objects.first()

    def get(self, request):
        if self.some:
            return render(request, 'guide_p/guide_home.html', {'some': self.some.station})
        return render(request, 'guide_p/guide_home.html', {})


class GuideList(ListView):

    def post(self, request):
        inputtxt = request.POST
        st = inputtxt['station']
        stations = Stations.objects.filter(station__icontains=st)
        return render(request, 'guide_p/stations_list.html', {'data': stations})

    def get_context_data(self, **kwargs):
        context = super(GuideList, self).get_context_data(**kwargs)
        self.limit = self.kwargs['limit']
        context['limit'] = self.limit
        return context

    template_name = 'guide_p/stations_list.html'
    context_object_name = 'data'
    allow_empty = True
    queryset = Stations.objects.all()

    def get_paginate_by(self, queryset):
        return self.kwargs['limit']


class GuideDetailView(DetailView):
    model = Stations


class StationFormView(View):

    def get(self, request):
        station_form = StationForm()
        return render(request, 'guide_p/add_station.html', {'station_form': station_form})

    def post(self, request):
        station_form = StationForm(request.POST)
        if station_form.is_valid():
            Stations.objects.create(**station_form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'guide_p/add_station.html', {'station_form': station_form})


class DeleteStationView(View):

    def get(self, request, id):
        try:
            station = Stations.objects.get(id=id)
            station.delete()
            return HttpResponseRedirect("/")
        except Stations.DoesNotExist:
            return HttpResponseNotFound("<h2>station not found или raise 'eror 404'</h2>")


def file_db(request):
    """
    передает содержимое файл css в модель БД Stations
    """
    from django.core.files.storage import FileSystemStorage

    for a in Stations.objects.all():
        a.delete()
    if request.method == 'POST':
        file_form = request.FILES.get('file_form')
        fs = FileSystemStorage()
        filename = fs.save(file_form.name, file_form)
        csv_dict_reader(filename)
        fs.delete(filename)
        return HttpResponseRedirect('/')


