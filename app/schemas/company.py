from pydantic import BaseModel

class Company(BaseModel):
    company: str
    industry: str
    country: str