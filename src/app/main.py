from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.app.router import ENVIRONMENT, router
from src.app.midlleware import Midlleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=ENVIRONMENT["origin"],
    allow_headers=["*"],
    allow_methods=["*"],
    allow_credentials=True
)

app.add_middleware(Midlleware)
app.include_router(router=router)