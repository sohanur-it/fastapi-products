from sqlalchemy import Column, String, Integer, ForeignKey, Float, ARRAY, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from ..db.database import Base

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    
    discount_percentage = Column(Float, nullable=True)
    rating = Column(Float, nullable=True)
    stock = Column(Integer, nullable=False)
    brand = Column(String, nullable=False)
    thumbnail = Column(String, nullable=False)
    images = Column(ARRAY(String), nullable=False)
    is_published = Column(Boolean, server_default="True", nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"), nullable=False)


    # new_type = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id', ondelete="CASCADE"), nullable=False)
    category = relationship("Category", back_populates="products")
    cart_items = relationship("CartItem", back_populates="product")
    
    # seller_id = Column(Integer, ForeignKey('seller.id'))
    # seller = relationship("Seller", back_populates='products')