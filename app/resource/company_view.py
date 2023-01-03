from uuid import UUID
from fastapi import APIRouter, HTTPException, status
from ..schemas.standar_response import HttpResponse
from ..schemas.company_schemas import CompanyDTO, CompanyResponse
from ..services.company_service import CompanyService

router = APIRouter(
        prefix='/company',
        tags=['company'],
        responses={404: {'description': 'Not found'}}
    )


@router.get('/list', response_model=list[CompanyResponse])
async def list_company():
    try:
        return await CompanyService.list_company()
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router.post('/create')
async def create_company(company: CompanyDTO):
    try:
        return await CompanyService.create_company(company)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

@router.delete('/delete/{id}')
async def create_company(id: UUID):
    try:
        return await CompanyService.delete_company(id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router.put('/update')
async def update_company(company: CompanyDTO):
    try:
        await CompanyService.update_company(company)
        return status.HTTP_200_OK
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

@router.get('/find/{id}', response_model=CompanyResponse)
async def get_one_bn(id: str):
    try:
        result = await CompanyService.get_company(id)
        if result is not None:
            return result
        else:
            raise
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)