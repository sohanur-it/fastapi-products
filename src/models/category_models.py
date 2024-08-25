from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import relationship
from ..db.database import Base


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    # new_name = Column(String)

    products = relationship("Product", back_populates="category")
