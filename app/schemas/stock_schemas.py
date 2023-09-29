import uuid
from datetime import date, datetime
from pydantic import BaseModel
from .company_schemas import CompanyStock
from ..models.stock_model import StockModel

class StockResponse(BaseModel):
    id: uuid.UUID
    company: CompanyStock
    stock_type: str
    operation_type: str
    bought_date: date
    value: float
    fee: float
    amount: float
    created: date
    updated: date

    class Config:
        orm_mode = True

class StockDTO(BaseModel):
    id: uuid.UUID | None = None
    company_id: uuid.UUID
    stock_type: str
    operation_type: str
    bought_date: date
    value: float
    fee: float | None = None
    amount: float
    updated: date | None = datetime.now()

    def modelMapper(self) -> StockModel:
        return StockModel(
            id=self.id,
            company_id=self.company_id,
            stock_type=self.stock_type,
            operation_type=self.operation_type,
            bought_date=self.bought_date,
            value=self.value,
            fee=self.fee,
            amount=self.amount,
            updated=self.updated
        )

    class Config:
        orm_mode = True
