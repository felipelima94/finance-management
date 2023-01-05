import uuid
from datetime import datetime
from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from ..database import Base

class CompanyModel(Base):
    __tablename__ = 'company'
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    fantasy_name = Column(String)
    administrator = Column(String)
    code = Column(String, nullable=False)
    cnpj = Column(String)
    created = Column(TIMESTAMP, nullable=False, default=datetime.now())
    updated = Column(TIMESTAMP, nullable=False, default=datetime.now())
    stocks = relationship('StockModel', back_populates='company')