from pydantic import BaseModel

#clase para la respuesta exitosa del login
class Token(BaseModel):
    access_token: str
    token_type: str

#clase para los datos dentro del token
class TokenData(BaseModel):
    username: str

#Informacion basica del usuario
class Usuario(BaseModel):
    username: str