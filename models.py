import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import ForeignKey, Column, Integer, String, CheckConstraint, DECIMAL

class Base(DeclarativeBase):
    pass

metadata = Base.metadata

class Category(Base):
    __tablename__ = 'categories'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(64), nullable=False, unique=True)
    products = relationship("Product", back_populates="categories")

    def __repr__(self):
        return f"name={self.name}"

class Product(Base):
    __tablename__ = 'products'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(64), nullable=False)
    price = Column(DECIMAL(precision=10, scale=2), CheckConstraint('price > 0'))
    quantity = Column(Integer, CheckConstraint('quantity > 0'))
    category_id = Column(UUID(as_uuid=True), ForeignKey('categories.id'), nullable=False)
    description = Column(String(64), nullable=True)
    categories = relationship('Category', back_populates='products')

    def __repr__(self):
        return f"name={self.name} price={self.price}"
