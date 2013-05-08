from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from crispy_forms.bootstrap import FormActions

from .models import Tour


class TourForm(forms.ModelForm):
    class Meta:
        model = Tour

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id_position'
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Fieldset(
                '',
                'tour_name',
                'tour_count',
            ),
            FormActions(
                Submit('submit', 'Add Tour', css_class="btn btn-primary")
            )
        )
        super(TourForm, self).__init__(*args, **kwargs)
