import logging
from uuid import UUID
from sqlalchemy.future import select
from sqlalchemy import update, delete, text

from ..models.stock_model import StockModel
from ..schemas.summary_schemas import SummaryDTO
from ..schemas.stock_schemas import StockResponse, StockDTO
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

    async def list_stock(self):
        async with async_session() as session:
            result = await session.execute(select(StockModel))
            transaction: list[StockDTO] = result.scalars().all()

            return self.__consolidate(transaction=transaction)

            
            return transaction
        
    def __consolidate(self, transaction: list[StockDTO]) -> list[SummaryDTO]:
        consolidated: list[SummaryDTO] = []
        for stock in transaction:
            if len(consolidated):
                found: int = 0

                for con in consolidated:
                    if stock.company.code == con.code:
                        found += 1
                        self.__calculate(con, stock)
                        break
                if not found:
                    summary: SummaryDTO = self.__create_summary_item(stock)
                    consolidated.append(summary)
            else:
                summary: SummaryDTO = self.__create_summary_item(stock)
                
                consolidated.append(summary)
        return consolidated
    
    def __create_summary_item(self, stock: StockDTO) -> SummaryDTO:
        return SummaryDTO(
                    code=stock.company.code,
                    amount=stock.amount,
                    stock_type=stock.stock_type,
                    total_invested=stock.value * stock.amount)
    
    def __calculate(self, summary: SummaryDTO, stock: StockDTO) -> SummaryDTO:
        if stock.operation_type != 'V':
            summary.amount += stock.amount
            summary.total_invested += stock.value * stock.amount
        elif stock.operation_type == 'V':
            summary.amount -= stock.amount
            summary.total_invested = (stock.value * stock.amount) - summary.total_invested
        
        return summary

    async def get_stock(id: UUID):
        async with async_session() as session:
            try:
                result = await session.get(StockModel, id)
                return result
            except Exception as e:
                logging.error(f'Error: get stock -> {e}')
                raise {'message': 'Opps, not found'}

    async def get_avg():
        try:
            file = open('app/services/sql/summary_stock.sql', 'r')
            sql = file.read()
        except Exception as e:
            logging.error(e)
        finally:
            file.close()

        async with async_session() as session:
            try:
                result = await session.execute(sql)
                return result.fetchall()
            except Exception as e:
                logging.error(f'Error: get prices -> {e}')