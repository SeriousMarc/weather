from django.views.generic import DetailView
from django.shortcuts import render

class WeatherDetailView(DetailView):
    template_name = 'base.html'

    def get(self, request):
        return render(request, self.template_name)
