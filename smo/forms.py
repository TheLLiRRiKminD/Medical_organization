from django import forms

from smo.models import Apppointment


class ApppointmentForm(forms.ModelForm):
    class Meta:
        model = Apppointment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_active':
                field.widget.attrs['class'] = 'form-control'
