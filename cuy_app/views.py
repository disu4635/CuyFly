from django.shortcuts import render
from .forms import FlightSearchForm, UserRegisterForm
from .models import Flight, Passenger, Ticket, Seat
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import random
import string

def home(request):
    try:
        # Intenta obtener el último Ticket ordenado por created_at
        latest_ticket = Ticket.objects.latest('created_at')
    except Ticket.DoesNotExist:
        # Si no hay ninguna instancia, establece un valor predeterminado o maneja de otra manera
        latest_ticket = None

    if latest_ticket:
        initial_values = {
            'origin': latest_ticket.flight.origin.city,  # Reemplaza 'origin' con el nombre real de tu campo
            'destination': latest_ticket.flight.destination.city,  # Reemplaza 'destination' con el nombre real de tu campo
        }
        form = FlightSearchForm(initial=initial_values)
        return render(request, 'home.html', {'form': form})

    return render(request, 'home.html', {'form': FlightSearchForm})

def select_fly(request):
    if request.method == 'POST':
        form = FlightSearchForm(request.POST)
        if form.is_valid():
            # Obtener datos del formulario
            origin = form.cleaned_data['origin']
            destination = form.cleaned_data['destination']
            # departure_date = form.cleaned_data['departure_date']
            # arrival_time = form.cleaned_data['arrival_time']
            flights = Flight.objects.filter(
                origin__city=origin,
                destination__city=destination,
            )
            return render(request, 'select_fly.html', {'flights': flights})

    else:
        form = FlightSearchForm()

    return render(request, 'home.html', {'form': form})

def generate_ref_no():
    # Genera un código único de 6 caracteres
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))


def create_ticket(request, flight_id):
    # Obtén el vuelo
    flight = get_object_or_404(Flight, id=flight_id)

    if request.method == 'POST':
        try:
            # Crea el ticket con el vuelo seleccionado
            ticket = Ticket.objects.create(flight=flight, ref_no=generate_ref_no())
            return JsonResponse({'ticket_id': ticket.id})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    # Devuelve un error si la solicitud no es POST
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def select_seat(request, ticket_id):
    # Obtén el ticket
    ticket = get_object_or_404(Ticket, id=ticket_id)

    # Renderiza la página de selección de asientos con el ticket
    return render(request, 'select_seat.html', {'ticket': ticket})

def update_ticket_add_seat(request, ticket_id, seat_number):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    try:
        # Intenta obtener el asiento existente
        seat = Seat.objects.get(seat_number=seat_number, is_reserved=True)

    except Seat.DoesNotExist:
        # Si el asiento no existe, créalo
        seat = Seat.objects.create(seat_number=seat_number, is_reserved=True)

    # Asigna el asiento al ticket
    ticket.seat = seat
    ticket.save()

    return JsonResponse({'ticket_id': ticket.id})

def select_mobile(request, ticket_id):
    # Obtén el ticket
    ticket = get_object_or_404(Ticket, id=ticket_id)
    try:
        if(len(Ticket.objects.all()) > 1):
            latest_ticket = Ticket.objects.all().order_by('-created_at')[1]
        else:
            latest_ticket = None
    except Ticket.DoesNotExist:
        latest_ticket = None
    
    if latest_ticket:
        last_mobile = latest_ticket.mobile
        return render(request, 'select_mobile.html', {'ticket': ticket, 'last_mobile': last_mobile})
    else:
        return render(request, 'select_mobile.html', {'ticket': ticket})

def update_ticket_mobile(request, ticket_id, option):
    try:
        ticket = get_object_or_404(Ticket, id=ticket_id)
        ticket.mobile = option
        ticket.save()
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'ticket_id': ticket.id})

def user_data_form(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return render(request, 'user_data_form.html', {'ticket':ticket,'form': UserRegisterForm})

def registro_view(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    form = UserRegisterForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['nombres']
        last = form.cleaned_data['apellidos']
        gender = form.cleaned_data['genero']
        email = form.cleaned_data['correo']
        flights = [ticket.flight]
        passenger = Passenger.objects.create(name=name, last=last, gender=gender)
        passenger.flights.set(flights)
        passenger.save()

        passengers = [passenger]
        ticket.passengers.set(passengers)
        ticket.email = email
        ticket.save()

    return render(request, 'payment.html', {'ticket_id': ticket_id})

def my_flights(request):
    tickets = Ticket.objects.all()
    return render(request, 'my_flights.html', {'tickets': tickets})
