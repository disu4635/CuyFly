from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.city} {self.code}"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()
    departure_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    arrival_time = models.TimeField(auto_now=False, auto_now_add=False)
    plane = models.CharField(max_length=24)    

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

GENDER = (
    ('male','MALE'),   
    ('female','FEMALE')
)

class Passenger(models.Model):
    name = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")
    gender = models.CharField(max_length=20, choices=GENDER, blank=True)
    
    def __str__(self):
        return f"{self.first}, {self.gender}"
    
class Seat(models.Model):
    seat_number = models.CharField(max_length=10, unique=True, help_text="Número de asiento")
    is_reserved = models.BooleanField(default=False, help_text="¿El asiento está reservado?")
    passenger = models.ForeignKey('Passenger', null=True, blank=True, on_delete=models.SET_NULL, related_name='seats', help_text="Pasajero asignado al asiento")

    def __str__(self):
        return self.seat_number

class Ticket(models.Model):
    ref_no = models.CharField(max_length=6, unique=True)
    passengers = models.ManyToManyField(Passenger, related_name="flight_tickets")
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="tickets", blank=True, null=True)
    flight_destination_date = models.DateField(blank=True, null=True)
    flight_arrival_date = models.DateField(blank=True, null=True)
    mobile = models.CharField(max_length=20,blank=True)
    email = models.EmailField(max_length=45, blank=True)

    def __str__(self):
        return self.ref_no

class Plane(models.Model):
    name = models.CharField(max_length=100, unique=True)
    capacity = models.PositiveIntegerField(help_text="Capacidad de pasajeros")
    registration_number = models.CharField(max_length=20, unique=True, help_text="Número de registro del avión")
    seats = models.ManyToManyField('Seat', related_name='planes', blank=True, help_text="Asientos disponibles en el avión")

    def __str__(self):
        return self.name