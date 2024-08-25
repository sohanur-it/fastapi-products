from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.orm import Session
from src.models import category_models
from src.schemas.category_scemas import *
from ..db.database import engine, get_db

from typing import List

router = APIRouter(
    prefix="/category"
)

category_models.Base.metadata.create_all(engine)


@router.get('', response_model=List[DisplayCategory])
async def category_list(db:Session=Depends(get_db)):
    category = db.query(category_models.Category).all()
    return category
