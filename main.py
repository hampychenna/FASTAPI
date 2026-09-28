from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import engine, Base, SessionLocal
import models
import curd
from schemas import BusCreate, BusResponse, BookingCreate, BookingResponse


app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "Bus Ticket Booking System"}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create Bus
@app.post("/buses", response_model=BusResponse)
def create_bus(bus: BusCreate, db: Session = Depends(get_db)):
    return curd.create_bus(db, bus)


# View All Buses
@app.get("/buses", response_model=list[BusResponse])
def get_buses(db: Session = Depends(get_db)):
    return curd.get_buses(db)


# Search Bus by Route
@app.get("/buses/search", response_model=list[BusResponse])
def search_buses(
    source: str,
    destination: str,
    db: Session = Depends(get_db)
):
    return curd.search_buses(db, source, destination)


# Get One Bus
@app.get("/buses/{bus_id}", response_model=BusResponse)
def get_bus(bus_id: int, db: Session = Depends(get_db)):
    bus = curd.get_bus(db, bus_id)

    if not bus:
        raise HTTPException(status_code=404, detail="Bus not found")

    return bus


# Create Booking
@app.post("/bookings", response_model=BookingResponse)
def create_booking(
    booking: BookingCreate,
    db: Session = Depends(get_db)
):
    result = curd.create_booking(db, booking)

    if not result:
        raise HTTPException(
            status_code=400,
            detail="Seat is already booked"
        )

    return result


# View All Bookings
@app.get("/bookings", response_model=list[BookingResponse])
def get_bookings(db: Session = Depends(get_db)):
    return curd.get_bookings(db)


# Cancel Booking
@app.delete("/bookings/{booking_id}")
def cancel_booking(
    booking_id: int,
    db: Session = Depends(get_db)
):
    result = curd.cancel_booking(db, booking_id)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    return {"message": "Booking cancelled successfully"}