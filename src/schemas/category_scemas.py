from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class DisplayCategory(BaseModel):
    id: int
    name : str

    class Config:
        from_attributes = True

