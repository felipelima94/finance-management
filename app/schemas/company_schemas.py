from uuid import UUID
from datetime import date, datetime
from pydantic import BaseModel
from ..models.company_model import CompanyModel

class CompanyResponse(BaseModel):
    id: UUID
    fantasy_name: str | None = None
    administrator: str | None = None
    code: str
    cnpj: str | None = None
    created: date
    updated: date

    class Config:
        orm_mode = True

class CompanyDTO(BaseModel):
    id: UUID | None = None
    fantasy_name: str | None = None
    administrator: str | None = None
    code: str
    cnpj: str | None = None
    updated: date | None = datetime.now()

    def modelMapper(self) -> CompanyModel:
        return CompanyModel(
            fantasy_name=self.fantasy_name,
            administrator=self.administrator,
            code=self.code,
            cnpj=self.cnpj
        )
    class Config:
        orm_mode = True

class CompanyStock(BaseModel):
    id: UUID
    code: str
    class Config:
        orm_mode = True