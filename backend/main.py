from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Trip(BaseModel):
    trip_id: int
    usr_id: int
    name: str

class TripUpdate(BaseModel):
    name: str

trips_db: dict[int, Trip] = {}
next_id: int = 0


@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/trips/")
def read_list_trip():
    return list(trips_db.values())

@app.get("/trips/{trip_id}")
def read_single_trip(trip_id: int):
    if trip_id in trips_db:
        return {"trip_name": trips_db[trip_id].name} 
    else:
        raise HTTPException(status_code=404, detail="Trip not found") 

@app.post("/trips/", status_code=201)
def create_trip(name: str):
    global next_id
    trips_db[next_id] = Trip(trip_id=next_id, usr_id=0, name=name)
    next_id = next_id+1
    return {"message": "Trip created!"}

@app.put("/trips/{trip_id}")
def update_trip(trip_id: int, trip_update: TripUpdate):
    if trip_id in trips_db:
        trips_db[trip_id].name = trip_update.name
        return trips_db[trip_id]
    else:
        raise HTTPException(status_code=404, detail="Trip not found") 

@app.delete("/trips/{trip_id}")
def delete_trip(trip_id: int):
    if trip_id in trips_db:
        del trips_db[trip_id]
        return {"Message": "Trip was deleted!"}
    else:
        raise HTTPException(status_code=404, detail="Trip not found") 