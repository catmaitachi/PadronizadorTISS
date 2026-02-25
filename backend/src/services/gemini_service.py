import threading, asyncio
from google import genai
from abc import ABC, abstractmethod
from src.config import config as env
from src.core.executor import obter_executor
from src.core.exceptions import AIError

class GeminiService(ABC):

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):

        with cls._lock:

            if cls._instance is None:
                
                cls._instance = super().__new__(cls)
                cls._instance.client = genai.Client(api_key=env.GEMINI_KEY)

        return cls._instance
    
    @abstractmethod
    async def processar_com_ia(self, conteudo: bytes, prompt: str) -> str: pass
    
class FileProcessingInterface(ABC):

    @abstractmethod
    async def criar_xml(self, conteudo: bytes) -> bytes: pass

class PDFService(GeminiService, FileProcessingInterface):

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):

        with cls._lock:

            if cls._instance is None:
                
                cls._instance = super().__new__(cls)

        return cls._instance
    
    async def processar_com_ia(self, conteudo: bytes, prompt: str = env.PDF_PROMPT) -> str:

        try:

            loop = asyncio.get_running_loop()

            resposta = await loop.run_in_executor( 
                
                obter_executor(),
                self.client.models.generate_content,
                model = "gemini-1.5-flash",
                contents = [ prompt, { "mime_type": "application/pdf", "data": conteudo } ]

            )

            if not resposta or not resposta.text: raise AIError("Resposta vazia do Gemini")

            return resposta.text

        except Exception as e: raise AIError(f"Gemini retornou um erro: {str(e)}") from e

    async def criar_xml( self, conteudo: bytes ) -> bytes: pass