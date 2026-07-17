from langchain_core.prompts import ChatPromptTemplate

research_prompt = ChatPromptTemplate.from_template("""
Eres un consultor especializado en SAP.

Analiza la siguiente empresa.

Empresa: {company}

Industria: {industry}

País: {country}

Devuelve un breve resumen.
""")