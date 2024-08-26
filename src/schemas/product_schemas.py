from pydantic import BaseModel, Field
from src.schemas.seller_schemas import DisplaySeller
from typing import Optional, List
from src.schemas.category_scemas import DisplayCategory
from datetime import datetime

class Product(BaseModel):
    name : str
    description: str
    price: int

class DisplayProduct(BaseModel):
    name: str
    description: str
    price: int
    category: DisplayCategory
    discount_percentage: float
    rating: float
    stock: int
    brand: str
    thumbnail: str
    images: List[str]
    is_published: bool
    created_at: datetime
    # seller: DisplaySeller

    class Config:
        from_attributes = True


class ProductRequest(BaseModel):
    name: str = Field(min_length=1)
    category_id: int = Field()
    description: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0)
    discount_percentage: float
    rating: float
    stock: int
    brand: str
    thumbnail: str
    images: List[str]
    is_published: bool
    created_at: datetime

    class Config:
        pass
        # json_schema_extra = {
        #     'example': {
        #         'name': 'Innovative Widget',
        #         'category': 'Widgets',
        #         'description': 'An innovative widget that solves all your widget needs',
        #         'price': 19.99
        #     }
        # }


