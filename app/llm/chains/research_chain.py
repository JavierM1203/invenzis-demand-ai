from app.llm.llm import llm
from app.llm.prompts.research_prompt import research_prompt
from app.schemas.research_response import ResearchResponse

structured_llm = llm.with_structured_output(
    ResearchResponse
)

research_chain = research_prompt | structured_llm