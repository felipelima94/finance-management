from fastapi import FastAPI, APIRouter
from .resource import company_view, stock_view

app = FastAPI()
router = APIRouter()

app.include_router(router=router)
app.include_router(company_view.router)
app.include_router(stock_view.router)

@router.get('/health')
def root():
    return {'message': 'IMOK'}
