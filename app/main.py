import uvicorn
from fastapi import FastAPI

from .User import user_controller


# 1. Cria a instância principal da nossa aplicação
app = FastAPI(
    title="API do Meu Projeto",
    version="0.1.0"
)

app.include_router(user_controller.router)

@app.get("/")
def read_root():
    return {"message": "API está no ar!"}

# 4. Código para rodar o servidor
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)