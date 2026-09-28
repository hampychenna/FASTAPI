from pydantic import BaseModel
from datetime import datetime


# Bus schema
class BusCreate(BaseModel):
    bus_name: str
    source: str
    destination: str
    total_seats: int


class BusResponse(BaseModel):
    id: int
    bus_name: str
    source: str
    destination: str
    total_seats: int

    class Config:
        from_attributes = True


# Booking schema
class BookingCreate(BaseModel):
    bus_id: int
    passenger_name: str
    seat_number: int


class BookingResponse(BaseModel):
    id: int
    bus_id: int
    passenger_name: str
    seat_number: int
    booking_date: datetime

    class Config:
        from_attributes = True