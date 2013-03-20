from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from .models import Position
from .forms import PositionForm


class PositionListView(ListView):
    template_name = 'positionlist.html'
    model = Position
    context_object_name = 'position_list'


class PositionDetailView(DetailView):
    template_name = 'positiondetail.html'
    context_object_name = 'position'


class PositionFormView(FormView):
    template_name = 'positionadd.html'
    form_class = PositionForm
    success_url = '/key_control/position/list/'

    def form_valid(self, form):
        super(PositionFormView, self).form_valid(form)
        form.save()
        return redirect(self.success_url)
