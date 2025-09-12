# app/clientes/controller.py
from fastapi import APIRouter, HTTPException, status

from .cliente_model import clienteCreate, clientePublic, clienteUpdate
from .cliente_repository import cliente_repository
from .cliente_service import cliente_service


router = APIRouter(prefix="/clientes", tags=["clientes"])

# Simulação de um banco de dados em memória
fake_db = {
    1: {"id": 1, "email": "cliente1@example.com", "full_name": "cliente One", "password": "password1"},
    2: {"id": 2, "email": "cliente2@example.com", "full_name": "cliente Two", "password": "password2"},
}

@router.post("/", response_model=clientePublic, status_code=status.HTTP_201_CREATED)
def create_cliente(cliente: clienteCreate):
    new_id = max(fake_db.keys() or [0]) + 1
    new_cliente_data = cliente.model_dump()
    new_cliente_data["id"] = new_id
    fake_db[new_id] = new_cliente_data
    return clientePublic(**new_cliente_data)

@router.get("/", response_model=list[clientePublic])
def list_clientes():
    # Converte os dicionários do 'banco de dados' para o modelo público
    return [clientePublic(**cliente_data) for cliente_data in fake_db.values()]

@router.put("/{cliente_id}", response_model=clientePublic)
def update_cliente(cliente_id: int, cliente_update: clienteUpdate):
    if cliente_id not in fake_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="cliente not found")

    stored_cliente_data = fake_db[cliente_id]
    update_data = cliente_update.model_dump(exclude_unset=True) # Apenas campos enviados

    updated_cliente = stored_cliente_data.copy()
    updated_cliente.update(update_data)
    fake_db[cliente_id] = updated_cliente

    return clientePublic(**updated_cliente)

@router.delete("/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cliente(cliente_id: int):
    if cliente_id not in fake_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="cliente not found")

    del fake_db[cliente_id]
    # Com status 204, a resposta não deve ter corpo. O FastAPI cuida disso.