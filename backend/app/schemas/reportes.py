from pydantic import BaseModel
from datetime import datetime
from typing import List

#Reporte de turnos por profesional
class ReporteTurnosPorProfesional(BaseModel):
    nombre: str
    apellido: str 
    especialidad: str
    total_turnos: int

#Reporte de profesionales sin turno
class ReporteProfesionalSinTurnos(BaseModel):
    nombre: str
    apellido: str
    especialidad: str

#Reporte para el listado de turnos pendientes
class ReporteTurnoCompleto(BaseModel):
    fecha_hora: datetime
    paciente_nombre_completo: str
    profesional_nombre_completo: str
    especialidad: str