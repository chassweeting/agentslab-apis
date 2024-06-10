from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..db.database import get_db
from ..db.models import OpeningHours
from .schemas import OpeningHoursSchema

router = APIRouter()


@router.get("/opening_hours", response_model=List[OpeningHoursSchema])
def get_all_opening_hours(db: Session = Depends(get_db)):
    """Get all opening hours"""
    return db.query(OpeningHours).all()


@router.get("/opening_hours/{day}", response_model=List[OpeningHoursSchema])
def get_opening_hours_by_day(day: str, db: Session = Depends(get_db)):
    """Get opening hours by day"""
    opening_hours = db.query(OpeningHours).filter(OpeningHours.day == day).all()
    if not opening_hours:
        raise HTTPException(status_code=404, detail="No opening hours found for this day")
    return opening_hours


@router.get("/special_opening_hours", response_model=List[OpeningHoursSchema])
def get_special_opening_hours(db: Session = Depends(get_db)):
    """Get special (VIP) opening hours"""
    return db.query(OpeningHours).filter(OpeningHours.is_special == True).all()
