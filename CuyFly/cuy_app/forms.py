from django import forms

class FlightSearchForm(forms.Form):
    origin = forms.CharField(widget=forms.Select(choices=[('Bogota', 'Bogota'), ('Cali', 'Cali'), ('Pasto', 'Pasto'), ('Ibague', 'Ibague'), ('Cartagena', 'Cartagena'), ('Pereira', 'Pereira')], attrs={'class': 'selectOrigen'}), required=False)
    destination = forms.CharField(widget=forms.Select(choices=[('Bogota', 'Bogota'), ('Cali', 'Cali'), ('Pasto', 'Pasto'), ('Ibague', 'Ibague'), ('Cartagena', 'Cartagena'), ('Pereira', 'Pereira')], attrs={'class': 'selectOrigen'}), required=False)
    departure_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'calendar-input'}), required=False)
    arrival_time = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'calendar-input'}), required=False)

class UserRegisterForm(forms.Form):
    TIPO_DOCUMENTO_CHOICES = [
        (1, 'Cedula de ciudadanía'),
        (2, 'Pasaporte'),
    ]

    GENERO_CHOICES = [
        (1, 'Masculino'),
        (2, 'Femenino'),
    ]

    tipo_documento = forms.ChoiceField(
        label='Tipo de documento',
        choices=TIPO_DOCUMENTO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'validationDefault04', 'required': True})
    )
    numero_documento = forms.CharField(
        label='Numero de documento',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'validationDefault05', 'required': True})
    )
    nombres = forms.CharField(
        label='Nombres',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'validationDefault01', 'required': True})
    )
    apellidos = forms.CharField(
        label='Apellidos',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'validationDefault02', 'required': True})
    )
    fecha_nacimiento = forms.DateField(
        label='Fecha de Nacimiento',
        widget=forms.DateInput(attrs={'class': 'form-control', 'id': 'validationDefaultUsername', 'required': True, 'type': 'date'})
    )
    genero = forms.ChoiceField(
        label='Genero',
        choices=GENERO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'validationDefault04', 'required': True})
    )

    correo = forms.EmailField(
        label='Correo',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'validationDefault01', 'required': True})
    )
    contraseña = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'validationDefault02', 'required': True})
    )

    agree_terms = forms.BooleanField(
        label='Agree to terms and conditions',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'invalidCheck2', 'required': True})
    )