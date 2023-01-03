from fastapi import FastAPI, APIRouter
from .models.company_model import CompanyModel
from .schemas.company_schemas import CompanyResponse, CompanyDTO
from .services.company_service import CompanyService
from .resource import company_view

app = FastAPI()
router = APIRouter()

app.include_router(router=router)
app.include_router(company_view.router)

@router.get('/health')
def root():
    return {'message': 'IMOK'}
