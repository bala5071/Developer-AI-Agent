from crewai import LLM
# from ollama import Ollama

def get_local_llm(model="llama3"):
    llm = LLM(model=f"ollama/{model}")
    return llm