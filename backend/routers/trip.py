from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.trip import Trip as TripModel
from schemas.trip import Trip as TripSchema
from schemas.trip import TripCreate, TripUpdate

router = APIRouter(prefix="/trips", tags=["trips"])

@router.get("/", response_model=list[TripSchema])
def read_list_trip(db: Session = Depends(get_db)):
    return db.query(TripModel).all()

@router.get("/{trip_id}", response_model=TripSchema)
def read_single_trip(trip_id: int, db: Session = Depends(get_db)):
    trip = db.query(TripModel).filter(TripModel.trip_id == trip_id).first()
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found") 
    return trip  

@router.post("/", response_model=TripSchema, status_code = 201)
def create_trip(newTrip: TripCreate, db:Session = Depends(get_db)):
    new_trip = TripModel(**newTrip.model_dump())
    db.add(new_trip)
    db.commit()
    db.refresh(new_trip)
    return new_trip

@router.put("/{trip_id}", response_model=TripSchema)
def update_trip(trip_id: int, trip_update: TripUpdate, db: Session = Depends(get_db)):
    updated_trip = db.query(TripModel).filter(TripModel.trip_id == trip_id).first()
    if not updated_trip:
        raise HTTPException(status_code=404, detail="Trip not found") 
    for key, value in trip_update.model_dump(exclude_unset=True).items():
        setattr(updated_trip, key, value)
    db.commit()
    db.refresh(updated_trip)
    return updated_trip

@router.delete("/{trip_id}", status_code=204)
def delete_trip(trip_id: int, db: Session = Depends(get_db)):
    trip = db.query(TripModel).filter(TripModel.trip_id == trip_id).first()
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found") 
    db.delete(trip)
    db.commit()