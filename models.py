from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


class Bus(Base):
    __tablename__ = "buses"

    id = Column(Integer, primary_key=True, index=True)
    bus_name = Column(String(100), nullable=False)
    source = Column(String(100), nullable=False)
    destination = Column(String(100), nullable=False)
    total_seats = Column(Integer, nullable=False)

    bookings = relationship("Booking", back_populates="bus")


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    bus_id = Column(Integer, ForeignKey("buses.id"), nullable=False)
    passenger_name = Column(String(100), nullable=False)
    seat_number = Column(Integer, nullable=False)
    booking_date = Column(DateTime, default=datetime.now)

    bus = relationship("bus", back_populates="booking")