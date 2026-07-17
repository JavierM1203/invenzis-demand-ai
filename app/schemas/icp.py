from pydantic import BaseModel

class ICP(BaseModel):

    country: str

    industry: str

    employees: int