from pydantic import BaseModel

class ProfesionalIn(BaseModel):
    matricula: str
    nombre: str
    apellido: str
    especialidad: str

class Profesional(ProfesionalIn):
    id: int

