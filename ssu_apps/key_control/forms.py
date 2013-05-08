from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div, HTML
from crispy_forms.bootstrap import FormActions

from .models import Position, Distribution


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position

    def clean_position(self):
        if self.cleaned_data['position'] > 9999:
            raise ValidationError('The position cannot be greater than 9999.')
        return self.cleaned_data['position']

    def __init__(self, *args, **kwargs):
        super(PositionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_position'
        # self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Fieldset(
                '',
                Div('position',
                    'keytype',
                    'keyway',
                    'status',
                    css_class="span4"
                    ),
                Div('notes',
                    css_class="span4"
                    ),
            ),
            FormActions(
                Submit('submit', 'Add Position', css_class="btn btn-primary")
            )
        )


class KeyIssueForm(forms.ModelForm):
    class Meta:
        model = Distribution
        fields = (
            'usertype',
            'userID',
            'fname',
            'lname',
            'department',
            # 'position',
            'sequence',
            'duedate',
            'notes',
        )

    def __init__(self, *args, **kwargs):
        super(KeyIssueForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_keyissueform'
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Fieldset(
                'Issue Keys',
                HTML('<h3>Identify Person to be Issued Keys'),
                'usertype',
                'userID',
                'fname',
                'lname',
                'department',
                HTML('<h3>Issue Key</h3>'),
                # 'position',
                'sequence',
                'duedate',
                'notes',
            ),
            FormActions(
                Submit('submit', 'Issue Key', css_class="btn btn-primary"),
            ),
        )
        self.fields['usertype'].required = True
        self.fields['fname'].required = True
        self.fields['lname'].required = True
        # self.fields['sequence'].choices = [('', '---------')]


class KeyFinderForm(forms.Form):
    # TODO: Define form fields here
    userID = forms.IntegerField(required=False)
    fname = forms.CharField(required=False)
    lname = forms.CharField(required=False)
    position = forms.IntegerField(required=False)
    sequence = forms.IntegerField(required=False)

    def __init__(self, *args, **kwargs):
        super(KeyFinderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'GET'
        self.helper.form_action = '/key_control/return/results/'
        self.helper.form_id = 'id_keyfinderform'
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Fieldset(
                'Key Finder Form',
                'userID',
                'fname',
                'lname',
                'position',
                'sequence',
            ),
            FormActions(
                Submit('submit', 'Look Up Keys', css_class="btn btn-primary")
            )
        )
        # self.fields['userID'].required = False
        # self.fields['fname'].required = False
        # self.fields['lname'].required = False
        # self.fields['position'].required = False
        # self.fields['sequence'].required = False


class KeyRenewForm(forms.ModelForm):
    class Meta:
        model = Distribution
        fields = ('duedate',)

    def __init__(self, *args, **kwargs):
        super(KeyRenewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_keyrenewform'
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Fieldset(
                'Enter a new due date for the key.',
                'duedate',
            ),
            FormActions(
                Submit('submit', 'Renew Key', css_class="btn btn-primary"),
            ),
        )


class KeysDueReportForm(forms.Form):
    # TODO: Define form fields here
    startdate = forms.DateField(required=False)
    enddate = forms.DateField(required=False)

    def __init__(self, *args, **kwargs):
        super(KeysDueReportForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'GET'
        self.helper.form_id = 'id_authenticationform'
        self.helper.form_class = 'form-inline'
        self.helper.layout = Layout(
            'startdate',
            'enddate',
            Submit('submit', 'Filter Report', css_class="btn btn-primary"),
        )


class SequenceStatusForm(forms.ModelForm):
    class Meta:
        model = Distribution
        fields = ('transtype', 'notes')

    def __init__(self, *args, **kwargs):
        super(SequenceStatusForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_sequencestatusform'
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Fieldset(
                '',
                'transtype',
                'notes',
            ),
            FormActions(
                Submit('submit', 'Log In', css_class="btn btn-primary"),
            ),
        )


class CrispyAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CrispyAuthenticationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_authenticationform'
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Fieldset(
                '',
                'username',
                'password',
            ),
            FormActions(
                Submit('submit', 'Log In', css_class="btn btn-primary"),
            ),
        )
