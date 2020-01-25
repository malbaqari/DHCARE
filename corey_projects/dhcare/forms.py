from django import forms

from .models import appointment


# By default DateInput takes input as string. Using this class, we can change the input as Calender
class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class getProviderInfo(forms.Form):
    OHP_Eth = forms.CharField(label='Hospital Ethereum Address', max_length=100)


class submitProviderInfo(forms.Form):
    name = forms.CharField(label='Hospital Name', max_length=100)
    webAddress = forms.CharField(label='Hospital Web Address', max_length=100)


class bookAppointment(forms.ModelForm):
    class Meta:
        model = appointment
        fields = ['name', 'nid', 'date', 'time', 'department_code']
        labels = {
            'name': 'Patient Name',
            'nid': 'National ID',
            'date': 'Date',
            'time': 'Time',
            'department_code': 'Clinic'
        }
        widgets = {'date': DateInput(), 'time': TimeInput()}


class getAppointments(forms.Form):
    nid = forms.IntegerField(label='Patient National ID')
