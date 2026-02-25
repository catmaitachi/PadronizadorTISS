import io
from fastapi import APIRouter, HTTPException, UploadFile, File
from fastapi.responses import StreamingResponse

router = APIRouter()

@router.post("/")
async def receber_arquivo( arquivo: UploadFile = File(...) ):
    
    if not arquivo.content_type == "application/pdf":

        raise HTTPException( status_code=400, detail="Apenas arquivos PDF são permitidos." )
    
    try:

        conteudo_bytes = await arquivo.read()

        xml = None  # todo - chamar controller para processar o arquivo e retornar a resposta

        buffer = io.BytesIO( xml.encode("utf-8") )    
        buffer.seek(0)

        return StreamingResponse ( buffer, media_type="application/xml", headers={ "Content-Disposition": f"attachment; filename={ arquivo.filename.replace('.pdf', '.xml') }" } )

    except Exception as e: raise HTTPException( status_code=500, detail=f"Erro ao ler o arquivo: {str(e)}" )
       

