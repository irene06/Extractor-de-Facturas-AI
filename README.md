# 🧾 Extractor de Facturas con IA (FastAPI + Groq)

API backend desarrollada con **FastAPI** y la inteligencia artificial de **Groq** (`qwen/qwen3.6-27b`) para extraer automáticamente datos clave de facturas a partir de capturas de pantalla o imágenes (JPG/PNG), sin necesidad de dependencias complejas de OCR local.

## 🚀 Características

* **Procesamiento Multimodal**: Utiliza las capacidades de visión de Groq para leer imágenes y capturas de factura de forma directa.
* **Estructura Estricta (JSON)**: Devuelve la información limpia y estructurada bajo un esquema Pydantic predefinido.
* **Sin Dependencias Pesadas**: Cero requerimientos de instalaciones locales conflictivas como Tesseract OCR o Poppler en Windows.
* **Documentación Interactiva**: Integración nativa con Swagger UI (`/docs`).

## 🛠️ Tecnologías Utilizadas

* **Python 3.10+**
* **FastAPI** (Framework web asíncrono)
* **Groq SDK** (Modelo multimodal `qwen/qwen3.6-27b`)
* **Pydantic** (Validación de datos y esquemas)
* **Uvicorn** (Servidor ASGI)
* **Python-dotenv** (Gestión de variables de entorno)

## ⚙️ Instalación y Configuración Local

1. **Cloná el repositorio:**
   ```bash
   git clone [https://github.com/irene06/Extractor-de-Facturas-AI.git](https://github.com/irene06/Extractor-de-Facturas-AI.git)
   cd Extractor-de-Facturas-AI
