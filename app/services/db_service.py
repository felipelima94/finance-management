import logging
from uuid import UUID
from sqlalchemy import update, delete
from ..database import async_session

class DbService:
    async def save(model) -> UUID:
        async with async_session() as session:
            try:
                cp = model.modelMapper()
                session.add(cp)
                await session.flush()
                await session.refresh(cp)
                return cp.id
            except Exception as e:
                logging.error(f'Error: create company -> {e}')
            finally:
                await session.commit()