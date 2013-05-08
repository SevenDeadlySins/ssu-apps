from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView

from braces.views import LoginRequiredMixin

from .models import Position, Sequence, Distribution, UserType, KeyType
from .forms import PositionForm, KeyIssueForm, KeyFinderForm


class PositionListView(LoginRequiredMixin, ListView):
    template_name = 'positionlist.html'
    model = Position
    context_object_name = 'position_list'


class PositionDetailView(LoginRequiredMixin, FormView):
    template_name = 'positiondetail.html'
    form_class = PositionForm

    def get_success_url(self, *args, **kwargs):
        return '/key_control/position/%s/' % self.kwargs['pk']

    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super(PositionDetailView, self).get_form_kwargs(*args, **kwargs)
        form_kwargs['instance'] = get_object_or_404(Position, pk=self.kwargs['pk'])
        return form_kwargs

    def get_context_data(self, *args, **kwargs):
        context = super(PositionDetailView, self).get_context_data(*args, **kwargs)
        position = get_object_or_404(Position, pk=self.kwargs['pk'])
        sequence_set = position.sequence_set.all()
        context['position'] = position
        context['issued'] = sequence_set.filter(issued=True)
        context['unissued'] = sequence_set.filter(issued=False)
        return context

    def form_valid(self, form):
        super(PositionDetailView, self).form_valid(form)
        position = form.save()
        return redirect(position)


class PositionFormView(LoginRequiredMixin, FormView):
    template_name = 'positionadd.html'
    form_class = PositionForm

    def form_valid(self, form):
        super(PositionFormView, self).form_valid(form)
        position = form.save()
        return redirect(position)


class CreateSequenceView(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        print "in CreateSequenceView"
        start_seq = int(request.GET['from'])
        end_seq = int(request.GET['to'])
        position = get_object_or_404(Position, pk=self.kwargs['pk'])
        for sequence_num in range(start_seq, end_seq+1):
            sequence = Sequence(position=position, sequence_num=sequence_num, issued=False)
            sequence.save()
            distribution = Distribution(position=position, sequence=sequence, transtype="CREATED", updater=request.user)
            distribution.save()
        return redirect(position)


class KeyIssueView(LoginRequiredMixin, FormView):
    template_name = 'keyissue.html'
    form_class = KeyIssueForm

    def form_valid(self, form):
        distribution = form.save(commit=False)
        distribution.position = distribution.sequence.position
        distribution.transtype = "ISSUED"
        distribution.updater = self.request.user
        distribution.save()
        sequence = distribution.sequence
        sequence.issued = True
        sequence.save()
        return redirect()


class KeyReturnView(LoginRequiredMixin, FormView):
    """docstring for KeyReturnView"""
    template_name = 'keyreturn.html'
    form_class = KeyFinderForm


class KeyReturnResultsView(TemplateView):
    """docstring for KeyReturnResultsView"""
    template_name = 'keyreturnresults.html'

    def get_context_data(self, *args, **kwargs):
        context = super(KeyReturnResultsView, self).get_context_data(*args, **kwargs)
        get = self.request.GET
        distributions = Distribution.objects.all()
        search_kwargs = {}
        for k, v in get.items():
            if k != "submit":
                if v:
                    kwarg = {'%s__contains' % k: v}
                    search_kwargs.update(kwarg)
        print search_kwargs
        distributions = distributions.filter(**search_kwargs)
        print distributions
        context['results'] = distributions
        return context


class UserTypeView(LoginRequiredMixin, ListView):
    template_name = 'usertype.html'
    model = UserType
    context_object_name = 'usertypes'


class KeyTypeView(LoginRequiredMixin, ListView):
    template_name = 'keytype.html'
    model = KeyType
    context_object_name = 'keytypes'
