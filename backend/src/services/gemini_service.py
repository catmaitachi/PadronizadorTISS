import asyncio
import functools
import io
import threading
from abc import ABC, abstractmethod

from google import genai
from google.genai import types

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
    async def processar_com_ia(self, conteudo: bytes, prompt: str, model: str = "gemini-flash-latest") -> str: pass
    
class FileProcessingInterface(ABC):

    @abstractmethod
    async def criar_xml(self, conteudo: bytes) -> bytes: pass

class PDFService(GeminiService, FileProcessingInterface):
    
    async def processar_com_ia(self, conteudo: bytes, prompt: str = env.PDF_PROMPT, model: str = "gemini-flash-latest") -> str:

        try:

            conteudo = types.Part.from_bytes( data = conteudo, mime_type = "application/pdf")
            prompt = types.Part.from_text( text = prompt )

            contents = [conteudo, prompt]

            func = functools.partial( self.client.models.generate_content, model=model, contents=contents )

            loop = asyncio.get_running_loop()
            
            resposta = await loop.run_in_executor( obter_executor(), func )

            if not resposta or not resposta.text: raise AIError("Resposta vazia do Gemini")

            return resposta.text

        except Exception as e: raise AIError(f"Gemini retornou um erro: {str(e)}") from e

    async def criar_xml( self, conteudo: bytes ) -> bytes: 

        gemini_resposta = await self.processar_com_ia( conteudo )

        # todo implementar gerador de XML

        