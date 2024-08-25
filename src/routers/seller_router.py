from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.orm import Session
from src.models import seller_models
from src.schemas.seller_schemas import Seller, DisplaySeller
from ..db.database import engine, get_db
from typing import List
from passlib.context import CryptContext


router = APIRouter(
    prefix="/seller"
)

# seller_models.Base.metadata.create_all(engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated='auto')

@router.get('', response_model=List[DisplaySeller])
async def get_seller(db: Session = Depends(get_db)):
    seller = db.query(seller_models.Seller).all()
    return seller

@router.post('', response_model=DisplaySeller)
async def post_seller(request: Seller, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(request.password)
    new_seller = seller_models.Seller(username=request.username, email=request.email, password=hashed_password)
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller