import threading
from google import genai
from src.config import env_config as env

class AIService:

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):

        with cls._lock:

            if cls._instance is None:
                
                cls._instance = super().__new__(cls)
                cls._instance.client = genai.Client(api_key=env.GEMINI_KEY)

        return cls._instance
    
    def processar_pdf( self, conteudo_pdf: bytes ) -> str:

        try:

            resposta = self.client.models.generate_content(

            model = "gemini-1.5-flash",
            contents = [ env.PROMPT, { "mime_type": "application/pdf", "data": conteudo_pdf } ]

            )

            return resposta.text

        except Exception as e: raise Exception(f"Erro ao processar PDF, ass Gemini: {str(e)}")