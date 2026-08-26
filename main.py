from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel, Field
from groq import Groq
import os
import json
import base64
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Extractor de Facturas AI (Groq)",
    description="API backend para procesar imágenes y PDFs de facturas usando Groq.",
    version="1.0"
)

# Usamos tu clave de Groq de siempre
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

class FacturaInfo(BaseModel):
    numero_factura: str = Field(description="Número oficial o código identificatorio de la factura")
    periodo: str = Field(description="Período fiscal o mes al que corresponde la factura")
    proveedor: str = Field(description="Nombre o razón social de la empresa emisora")

@app.post("/extraer-factura/", response_model=FacturaInfo)
async def extraer_factura(file: UploadFile = File(...)):
    if file.content_type not in ["application/pdf", "image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Formato no soportado. Subí una imagen (JPG/PNG) o un PDF.")
    
    try:
        contenido_bytes = await file.read()
        
        # Si es una imagen, la codificamos en base64 para enviarla a Groq Vision
        if file.content_type in ["image/jpeg", "image/png"]:
            imagen_base64 = base64.b64encode(contenido_bytes).decode('utf-8')
            
            # Llamada  Groq (Llama 3.2 11B Vision soporta imágenes perfectamente)
            completion = client.chat.completions.create(
                model="qwen/qwen3.6-27b",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text", 
                                "text": "Extrae los datos de esta factura. Responde ÚNICAMENTE en formato JSON válido con las claves exactas: numero_factura, periodo, proveedor."
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:{file.content_type};base64,{imagen_base64}"
                                }
                            }
                        ]
                    }
                ],
                response_format={"type": "json_object"}
            )
        else:
            # pdf
            raise HTTPException(status_code=400, detail="Por favor, subí la captura de pantalla o imagen (JPG/PNG) de la factura.")
        
        respuesta_json = json.loads(completion.choices[0].message.content)
        return respuesta_json

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error detallado: {str(e)}")