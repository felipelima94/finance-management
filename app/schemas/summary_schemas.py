from pydantic import BaseModel
import decimal


class SummaryDTO(BaseModel):
    code: str
    stock_type: str
    amount: decimal.Decimal
    total_invested: decimal.Decimal

    class Config:
        orm_mode = True