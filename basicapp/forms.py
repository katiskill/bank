from django.utils import timezone
from django import forms
from django.core.exceptions import ValidationError

from .models import OperationStatus


class OperationStatusModelForm(forms.ModelForm):
    def clean_end_time(self):
        data = self.cleaned_data['end_time']

        # check if a date is not in the past
        if data < timezone.now():
            raise ValidationError('Invalid time - end time in the past')

        return data

    class Meta:
        model = OperationStatus
        fields = ('__all__')
        help_texts = {
            'start_time': 'Format: 2006-10-25 14:30:59.000200',
            'end_time': 'Format: 2006-10-26 15:30:59.000200',
        }
