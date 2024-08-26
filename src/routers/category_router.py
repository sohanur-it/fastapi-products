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


@router.post('', status_code=status.HTTP_201_CREATED)
async def add(category_request: CategoryCreate, db: Session= Depends(get_db)):
    # category = db.query(category_models.Category).filter(category_models.Category.id == category_request.id).first()
    # if not category:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    new_category = category_models.Category(**category_request.model_dump())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category
