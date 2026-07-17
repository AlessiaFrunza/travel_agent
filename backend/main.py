from fastapi import FastAPI, HTTPException
from routers import trip

app = FastAPI()
app.include_router(trip.router)


