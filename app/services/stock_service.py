import logging
from uuid import UUID
from sqlalchemy.future import select
from sqlalchemy import update, delete

from ..models.stock_model import StockModel
from ..schemas.stock_schemas import StockDTO
from ..database import async_session
from .db_service import DbService

class StockService:

    async def create_stock(stock: StockDTO):
        return await DbService.save(stock)
        # async with async_session() as session:
        #     try:
        #         session.add(stock.stockModelMapper())
        #         await session.commit()
        #     except Exception as e:
        #         logging.error(f'Erro: create stock -> {e}')
        #         await session.rollback()

    async def update_stock(stock: StockDTO):
        async with async_session() as session:
            try:
                await session.execute(update(StockModel).where(StockModel.id==stock.id).values(stock.dict()))
                return await session.commit()
            except Exception as e:
                logging.error(f'Error: Update stock -> {e}')
                await session.rollback()
                raise
    
    async def delete_stock(stock_id: UUID):
        async with async_session() as session:
            try:
                exist = await session.execute(select(StockModel).where(StockModel.id==stock_id))
                if exist.scalar():
                    await session.execute(
                        delete(StockModel).where(StockModel.id==stock_id)
                    )
                    return await session.commit()
                else:
                    raise {'message': 'Not found'}
            except Exception:
                await session.rollback()
                raise {'message': 'Opps, something happened'}

    async def list_stock():
        async with async_session() as session:
            result = await session.execute(select(StockModel))
            return result.scalars().all()

    async def get_stock(id: UUID):
        async with async_session() as session:
            try:
                result = await session.get(StockModel, id)
                return result
            except Exception as e:
                logging.error(f'Error: get stock -> {e}')
                raise {'message': 'Opps, not found'}