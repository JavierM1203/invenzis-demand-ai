from fastapi import APIRouter

from app.schemas.company import Company
from app.services.research_service import ResearchService

router = APIRouter()

service = ResearchService()


@router.post("/research")
def research(company: Company):

    return service.generate(company)