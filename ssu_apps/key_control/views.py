from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import View, ListView, TemplateView
from django.views.generic.edit import FormView

from braces.views import LoginRequiredMixin

from .models import Position, Sequence, Distribution, UserType, KeyType
from .forms import PositionForm, KeyIssueForm, KeyFinderForm, KeyRenewForm, KeysDueReportForm, SequenceStatusForm


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

    def get_success_url(self, *args, **kwargs):
        return '/key_control/position/list/'

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
        return redirect(distribution.position)


class KeyReturnFinderView(LoginRequiredMixin, FormView):
    """docstring for KeyReturnView"""
    template_name = 'keyreturn.html'
    form_class = KeyFinderForm


class KeyReturnResultsView(TemplateView):
    """docstring for KeyReturnResultsView"""
    template_name = 'keyreturnresults.html'

    def get_context_data(self, *args, **kwargs):
        context = super(KeyReturnResultsView, self).get_context_data(*args, **kwargs)
        get = self.request.GET
        current_distributions = []
        for sequence in Sequence.objects.filter(issued=True):
            current_distributions.append(sequence.get_current_distribution().id)
        distribution_set = Distribution.objects.filter(pk__in=current_distributions)
        search_kwargs = {}
        for k, v in get.items():
            if k != "submit":
                if v:
                    kwarg = {'%s__contains' % k: v}
                    search_kwargs.update(kwarg)
        print search_kwargs
        distribution_set = distribution_set.filter(**search_kwargs)
        print distribution_set
        context['results'] = distribution_set
        return context


class KeyReturnView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        distribution = get_object_or_404(Distribution, pk=self.kwargs['pk'])
        sequence = distribution.sequence
        sequence.issued = False
        sequence.save()
        new_distribution = Distribution(position=distribution.position, sequence=distribution.sequence, transtype="RETURNED", updater=request.user)
        new_distribution.save()
        return redirect('/key_control/')


class KeyRenewView(LoginRequiredMixin, FormView):
    template_name = 'keyrenew.html'
    form_class = KeyRenewForm

    def form_valid(self, form):
        old_distribution = Distribution.objects.get(pk=self.kwargs['pk'])
        new_distribution = form.save(commit=False)
        new_distribution.transtype = "RENEWED"
        new_distribution.updater = self.request.user
        new_distribution.position = old_distribution.position
        new_distribution.sequence = old_distribution.sequence
        new_distribution.userID = old_distribution.userID
        new_distribution.usertype = old_distribution.usertype
        new_distribution.fname = old_distribution.fname
        new_distribution.lname = old_distribution.lname
        new_distribution.department = old_distribution.department
        new_distribution.notes = old_distribution.notes
        new_distribution.save()
        sequence = new_distribution.sequence
        sequence.issued = True
        sequence.save()
        return redirect(new_distribution.position)


class SequenceDeleteView(LoginRequiredMixin, View):
    """docstring for SequenceDeleteView"""
    def get(self, request, *args, **kwargs):
        sequence = get_object_or_404(Sequence, pk=self.kwargs['pk'])
        if sequence.issued:
            raise PermissionDenied
        position = sequence.position
        sequence.delete()
        return redirect(position)


class DistributionListView(LoginRequiredMixin, ListView):
    template_name = 'distributionlist.html'
    model = Distribution
    paginate_by = 20
    context_object_name = 'distribution_list'


class KeysDueReportView(LoginRequiredMixin, ListView):
    template_name = 'keysduereport.html'
    model = Distribution
    paginate_by = 20
    context_object_name = 'distribution_list'

    def get_queryset(self, *args, **kwargs):
        current_distributions = []
        for sequence in Sequence.objects.filter(issued=True):
            current_distributions.append(sequence.get_current_distribution().id)
        distribution_set = Distribution.objects.filter(pk__in=current_distributions)
        if self.request.GET.get('startdate'):
            startdate = self.request.GET.get('startdate')
            distribution_set = distribution_set.filter(duedate__gte=startdate)
        if self.request.GET.get('enddate'):
            enddate = self.request.GET.get('enddate')
            distribution_set = distribution_set.filter(duedate__lte=enddate)
        return distribution_set

    def get_context_data(self, *args, **kwargs):
        context = super(KeysDueReportView, self).get_context_data(*args, **kwargs)
        context['form'] = KeysDueReportForm(self.request.GET)
        return context


class SequenceStatusView(LoginRequiredMixin, FormView):
    template_name = "sequencestatus.html"
    form_class = SequenceStatusForm

    def form_valid(self, form):
        sequence = get_object_or_404(Sequence, pk=self.kwargs['pk'])
        distribution = form.save(commit=False)
        distribution.sequence = sequence
        distribution.position = sequence.position
        distribution.updater = self.request.user
        distribution.save()
        sequence.issued = False
        sequence.save()
        return redirect(distribution.position)


class UserTypeView(LoginRequiredMixin, ListView):
    template_name = 'usertype.html'
    model = UserType
    context_object_name = 'usertypes'


class KeyTypeView(LoginRequiredMixin, ListView):
    template_name = 'keytype.html'
    model = KeyType
    context_object_name = 'keytypes'
