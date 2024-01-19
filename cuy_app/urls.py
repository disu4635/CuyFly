from django.urls import path
from .views import home, select_fly, select_seat, create_ticket, update_ticket_add_seat, select_mobile, update_ticket_mobile,user_data_form, registro_view, my_flights

urlpatterns = [
    path('', home, name='home'),
    path('select_fly/', select_fly, name='select_fly'),
    path('create_ticket/<int:flight_id>/', create_ticket, name='create_ticket'),
    path('select_seat/<int:ticket_id>/', select_seat, name='select_seat'),
    path('update_ticket/<int:ticket_id>/add_seat/<str:seat_number>/', update_ticket_add_seat, name='actualizar_ticket_add_seat'),
    path('select_mobile/<int:ticket_id>/',select_mobile , name='select_mobile'),
    path('update_ticket_mobile/<int:ticket_id>/<str:option>/',update_ticket_mobile, name="update_ticket_mobile"),
    path('user_data_form/<int:ticket_id>', user_data_form, name="user_data_form"),
    path('user_payment_form/<int:ticket_id>', registro_view, name="user_payment_form"),
    path('my_flights', my_flights, name="my_flights")
]