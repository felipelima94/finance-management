from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from .resource import company_view, stock_view

app = FastAPI()
router = APIRouter()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=router)
app.include_router(company_view.router)
app.include_router(stock_view.router)

@router.get('/health')
def root():
    return {'message': 'IMOK'}
