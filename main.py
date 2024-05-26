from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from controller import session_router,user_router,role_router,regiao_router,cidade_router,tipo_escola_router

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(session_router)
app.include_router(user_router)
app.include_router(role_router)
app.include_router(regiao_router)
app.include_router(cidade_router)
app.include_router(tipo_escola_router)

uvicorn.run(app,host='0.0.0.0',port=8080)