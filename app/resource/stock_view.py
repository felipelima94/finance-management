from uuid import UUID
from fastapi import APIRouter, HTTPException, status
from ..schemas.stock_schemas import StockResponse, StockDTO
from ..services.stock_service import StockService

router = APIRouter(
        prefix='/stock',
        tags=['stock'],
        responses={404: {'description': 'Not found'}}
    )


@router.get('/list', response_model=list[StockResponse])
async def list_stock():
    try:
        return await StockService.list_stock()
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router.post('/create')
async def create_stock(stock: StockDTO):
    try:
        return await StockService.create_stock(stock)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

@router.delete('/delete/{id}')
async def delete_stock(id: UUID):
    try:
        return await StockService.delete_stock(id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router.put('/update')
async def update_stock(stock: StockDTO):
    try:
        await StockService.update_stock(stock)
        return status.HTTP_200_OK
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

@router.get('/find/{id}', response_model=StockResponse)
async def get_stock(id: str):
    try:
        result = await StockService.get_stock(id)
        if result is not None:
            return result
        else:
            raise
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)