# Create your views here.
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from .models import Tour
from .forms import TourForm


class TourListView(ListView):
    template_name = 'positionlist.html'
    model = Tour
    context_object_name = 'tour_list'


class TourDetailView(DetailView):
    template_name = 'positiondetail.html'
    model = Tour
    context_object_name = 'tour'


class TourFormView(FormView):
    template_name = 'positionadd.html'
    form_class = TourForm
    success_url = '/key_control/tour/list/'

    def form_valid(self, form):
        super(PositionFormView, self).form_valid(form)
        form.save()
        return redirect(self.success_url)
