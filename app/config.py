import os
from dotenv import load_dotenv


load_dotenv()

class settings:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")    

    QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
    QDRANT_URL = os.getenv("QDRANT_CLUSTER_ENDPOINT")
    QDRANT_URL="PRAG"

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GROQ_FALLBACK_API_KEY = os.getenv("GROQ_FALLBACK_API_KEY")
    GROQ_MODEL="llma-3.3-70b-versatile"
    
Settings=settings()
                