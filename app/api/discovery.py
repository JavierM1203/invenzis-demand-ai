from fastapi import APIRouter
from app.schemas.icp import ICP
from app.services.discovery_service import DiscoveryService

router = APIRouter()

service = DiscoveryService()


@router.post("/discover")
def discover(icp: ICP):

    return service.discover(icp)