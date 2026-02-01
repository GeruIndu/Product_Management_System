from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import ForeignKey, Column, Integer, String, CheckConstraint, DECIMAL

class Base(DeclarativeBase):
    pass

metadata = Base.metadata

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, unique=True)
    products = relationship("Product", back_populates="categories")

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    price = Column(DECIMAL(precision=10, scale=2), CheckConstraint('price > 0'))
    quantity = Column(Integer, CheckConstraint('quantity > 0'))
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    categories = relationship('Category', back_populates='products')
