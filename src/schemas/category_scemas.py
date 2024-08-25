from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class DisplayCategory(BaseModel):
    name : str

    class Config:
        from_attributes = True

