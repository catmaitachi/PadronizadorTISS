import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Gemini API

GEMINI_KEY = os.getenv("GEMINI_API_KEY")

# Prompts

PDF_PROMPT = os.getenv("PDF_PROMPT")

# Detalhes do Projeto

NAME = os.getenv("NAME")
VERSION = os.getenv("VERSION")
DESCRIPTION = os.getenv("DESCRIPTION")

# Configuração da API

HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8000))
RELOAD = os.getenv("RELOAD", "True").lower() == "true"
THREADS = int(os.getenv("THREADS", 10))