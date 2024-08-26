from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.orm import Session
from src.models import product_models, category_models
from src.schemas.product_schemas import *
from ..db.database import engine, get_db
from src.schemas.seller_schemas import Seller
from src.routers.login_router import get_current_user
from typing import List

router = APIRouter(
    prefix="/products"
)

product_models.Base.metadata.create_all(engine)


@router.get('', response_model=List[DisplayProduct])
async def product_list(db:Session=Depends(get_db)):
    products = db.query(product_models.Product).all()
    return products

@router.get('/{id}', response_model=DisplayProduct)
def get_product(id, db: Session = Depends(get_db)):
    product = db.query(product_models.Product).filter(product_models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with ID {id} not found")
    return product

@router.post('', status_code=status.HTTP_201_CREATED)
async def add(product_request: ProductRequest, db: Session= Depends(get_db)):
    category = db.query(category_models.Category).filter(category_models.Category.id == product_request.category_id).first()
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    new_product = product_models.Product(**product_request.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.put('/{id}')
async def update(id, request: Product, db:Session = Depends(get_db)):
    product = db.query(product_models.Product).filter(product_models.Product.id == id)
    if not product.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with ID {id} not found")
    product.update(request.dict())
    db.commit()
    return {'updated'}
    

