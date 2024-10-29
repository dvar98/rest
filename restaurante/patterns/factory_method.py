# patterns/factory_method.py
from ..models import Reserva

class ReservaFactory:
    @staticmethod
    def create_reserva(fecha, hora, estado, usuario, mesa):
        return Reserva(fecha=fecha, hora=hora, estado=estado, usuario=usuario, mesa=mesa)