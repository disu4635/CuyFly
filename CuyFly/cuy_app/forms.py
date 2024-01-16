from django import forms

class FlightSearchForm(forms.Form):
    origin = forms.CharField(widget=forms.Select(choices=[('Bogota', 'Bogota'), ('Cali', 'Cali')], attrs={'class': 'selectOrigen'}), required=False)
    destination = forms.CharField(widget=forms.Select(choices=[('Bogota', 'Bogota'), ('Cali', 'Cali')], attrs={'class': 'selectOrigen'}), required=False)
    departure_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'calendar-input'}), required=False)
    arrival_time = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'calendar-input'}), required=False)