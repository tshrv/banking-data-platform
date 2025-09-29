from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from provisioning_service.router import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_credentials=True,
    allow_headers=["*"],
)

app.include_router(router=router)
