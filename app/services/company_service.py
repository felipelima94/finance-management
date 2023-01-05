import logging
from uuid import UUID
from sqlalchemy.future import select
from sqlalchemy import update, delete

from .db_service import DbService
from ..models.company_model import CompanyModel
from ..schemas.company_schemas import CompanyDTO
from ..database import async_session

class CompanyService:

    async def create_company(company: CompanyDTO):
        return await DbService.save(company)

    async def update_company(company: CompanyDTO):
        async with async_session() as session:
            try:
                await session.execute(update(CompanyModel).where(CompanyModel.id==company.id).values(company.dict()))
                return await session.commit()
            except Exception:
                await session.rollback()
                raise
    
    async def delete_company(company_id: UUID):
        async with async_session() as session:
            try:
                exist = await session.execute(select(CompanyModel).where(CompanyModel.id==company_id))
                if exist.scalar():
                    await session.execute(
                        delete(CompanyModel).where(CompanyModel.id==company_id)
                    )
                    return await session.commit()
                else:
                    raise {'message': 'Not found'}
            except Exception:
                await session.rollback()
                raise {'message': 'Opps, something happened'}

    async def list_company():
        async with async_session() as session:
            result = await session.execute(select(CompanyModel))
            return result.scalars().all()

    async def get_company(id: UUID):
        async with async_session() as session:
            try:
                # result = await session.execute(select(CompanyModel).where(CompanyModel.id==id))
                result = await session.get(CompanyModel, id)
                return result
            except Exception:
                raise {'message': 'Opps, not found'}