import threading
from fastapi import HTTPException, UploadFile
from src.services.gemini_service import PDFService
from src.core import exceptions as exc

class Controller:

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):

        with cls._lock:

            if cls._instance is None:
                
                cls._instance = super().__new__(cls)

        return cls._instance
    
    async def arquivo_para_xml( self, arquivo: UploadFile ):

        try: 
        
            match arquivo.content_type:

                case "application/pdf": 
                    
                    arquivo_bytes = await arquivo.read()
                    
                    return await PDFService().criar_xml( arquivo_bytes )

                case _: raise HTTPException(status_code=415, detail="Tipo de arquivo não suportado")

        except exc.AIError as e: raise HTTPException(status_code=502, detail=f"Erro no serviço de IA: {str(e)}")
        except exc.ConfigError as e: raise HTTPException(status_code=500, detail=f"Erro de configuração: {str(e)}")
        except exc.APIError as e: raise HTTPException(status_code=500, detail=f"Erro na API: {str(e)}")
        except IOError as e: raise HTTPException(status_code=400, detail=f"Erro ao ler o arquivo: {str(e)}")
        except Exception as e: raise HTTPException(status_code=500, detail=f"Erro interno do servidor: {str(e)}")