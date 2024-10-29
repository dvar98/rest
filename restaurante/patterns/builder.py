# patterns/builder.py
from ..models import Reserva

class ReservaBuilder:
    def __init__(self):
        self.reserva = Reserva()

    def set_fecha(self, fecha):
        self.reserva.fecha = fecha
        return self

    def set_hora(self, hora):
        self.reserva.hora = hora
        return self

    def set_estado(self, estado):
        self.reserva.estado = estado
        return self

    def set_usuario(self, usuario):
        self.reserva.usuario = usuario
        return self

    def set_mesa(self, mesa):
        self.reserva.mesa = mesa
        return self

    def build(self):
        self.reserva.save()
        return self.reserva