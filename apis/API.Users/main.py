from fastapi import FastAPI

# Crie a aplicação FastAPI
app = FastAPI()

# Importando e incluindo os controladores
from controllers import user_controller

# Incluindo os routers dos controladores na aplicação
app.include_router(user_controller.router)

# Isso faz com que cada rota definida nos controladores seja registrada na aplicação
