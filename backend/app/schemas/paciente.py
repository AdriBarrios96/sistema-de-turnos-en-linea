from pydantic import BaseModel, EmailStr

#Crea o actualiza un paciente
class PacienteIn(BaseModel):
    dni: int
    nombre: str
    apellido: str
    telefono: str
    email: EmailStr

#Devuelve un paciente con el ID 
class Paciente(PacienteIn):
    id: int
