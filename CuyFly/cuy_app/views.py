from django.shortcuts import render
from .forms import FlightSearchForm
from .models import Flight

def home(request):
    return render(request, 'home.html', {'form': FlightSearchForm})

def select_fly(request):
    if request.method == 'POST':
        form = FlightSearchForm(request.POST)
        if form.is_valid():
            # Obtener datos del formulario
            origin = form.cleaned_data['origin']
            destination = form.cleaned_data['destination']
            departure_date = form.cleaned_data['departure_date']
            arrival_time = form.cleaned_data['arrival_time']
            flights = Flight.objects.filter(origin__city=origin, 
                                                      destination__city=destination, 
                                                      departure_datetime__date=departure_date, 
                                                      arrival_time=arrival_time)
            # Renderizar la plantilla con los resultados
            return render(request, 'select_fly.html', {'flights': flights})
    else:
        form = FlightSearchForm()

    return render(request, 'home.html', {'form': form})