import uuid
from datetime import datetime
from sqlalchemy import Column, String, ForeignKey, TIMESTAMP, Numeric, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from ..database import Base

class StockModel(Base):
    __tablename__ = 'stock'
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    company_id = Column(UUID(as_uuid=True), ForeignKey('company.id'), nullable=False)
    company = relationship('CompanyModel', back_populates="stocks", lazy="subquery")
    stock_type = Column(String, nullable=False)
    operation_type = Column(String, nullable=False)
    bought_date = Column(TIMESTAMP, nullable=False)
    value = Column(Numeric, nullable=False)
    fee = Column(Numeric)
    amount = Column(Integer, nullable=False)
    created = Column(TIMESTAMP, nullable=False, default=datetime.now())
    updated = Column(TIMESTAMP, nullable=False, default=datetime.now())