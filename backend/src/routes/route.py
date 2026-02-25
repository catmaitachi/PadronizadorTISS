import io

from fastapi import APIRouter, File, UploadFile
from fastapi.responses import StreamingResponse

from src.controllers.controller import Controller

router = APIRouter()

@router.post( "/xml", response_class=StreamingResponse )
async def receber_arquivo( arquivo: UploadFile = File(...) ):

    xml = await Controller.arquivo_para_xml( arquivo )

    buffer = io.BytesIO( xml.encode("utf-8") )    
    buffer.seek(0)

    return StreamingResponse ( buffer, media_type="application/xml", headers={ "Content-Disposition": f"attachment; filename={ arquivo.filename.replace('.pdf', '.xml') }" } )

       

