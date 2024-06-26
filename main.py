from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from controller import query_router,session_router,user_router,role_router,regiao_router,cidade_router,tipo_escola_router,unidade_escolar_router,endereco_router

app = FastAPI()

origins = ["http://localhost:5173"]

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
app.include_router(unidade_escolar_router)
app.include_router(endereco_router)
app.include_router(query_router)

uvicorn.run(app,host='0.0.0.0',port=7860)