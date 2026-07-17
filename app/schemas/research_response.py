from pydantic import BaseModel

class ResearchResponse(BaseModel):

    summary: str

    pain_points: list[str]

    opportunities: list[str]

    digital_maturity: str