# app/cliente/models.py
from pydantic import BaseModel, EmailStr, Field

# Schema para os dados que o cliente envia ao CRIAR um cliente
class ClienteCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    full_name: str | None = Field(default=None, min_length=3)

# Schema para os dados que o cliente envia ao ATUALIZAR um usuário
# Todos os campos são opcionais
class ClienteUpdate(BaseModel):
    email: EmailStr | None = None
    password: str | None = Field(default=None, min_length=8)
    full_name: str | None = Field(default=None, min_length=3)

# Schema para os dados que a API RETORNA ao cliente (público)
class ClientePublic(BaseModel):
    id: int
    email: EmailStr
    full_name: str | None = None