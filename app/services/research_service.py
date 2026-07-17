from app.schemas.company import Company
from app.llm.llm import llm
from app.llm.chains.research_chain import research_chain

class ResearchService:

    def generate(self, company):

        response = research_chain.invoke({

            "company": company.company,

            "industry": company.industry,

            "country": company.country

        })

        return response