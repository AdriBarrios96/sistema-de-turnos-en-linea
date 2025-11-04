from pydantic import BaseModel
from datetime import datetime

#Recibe datos y los almacena
class TurnoCreate(BaseModel):
    paciente_id: int
    profesional_id: int
    fecha_hora: datetime #Vuelve el string del frontend a datetime

class TurnoAsignarSP(TurnoCreate):
    pass

#Devuelve un turno
class Turno(TurnoCreate):
    id: int
    estado: str = "Pendiende" #pueden ser: 'Pendiente', 'Confirmado', 'Cancelado', 'Realizado'