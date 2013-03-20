from django import forms
from django.core.exceptions import ValidationError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from crispy_forms.bootstrap import FormActions

from .models import Position


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position

    def clean_position(self):
        if self.cleaned_data['position'] > 9999:
            raise ValidationError('The position cannot be greater than 9999.')
        return self.cleaned_data['position']

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id_position'
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Fieldset(
                '',
                'position',
                'keytype',
                'keyway',
                'status',
                'notes',
            ),
            FormActions(
                Submit('submit', 'Add Position', css_class="btn btn-primary")
            )
        )
        super(PositionForm, self).__init__(*args, **kwargs)
