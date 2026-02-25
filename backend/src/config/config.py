import os
from pathlib import Path
from dotenv import load_dotenv
from src.core.exceptions import ConfigError

load_dotenv()

# Gemini API

GEMINI_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_KEY: raise ConfigError("GEMINI_API_KEY não definida no .env")

# Prompts

PDF_PROMPT = os.getenv("PDF_PROMPT")

if not PDF_PROMPT: raise ConfigError("PDF_PROMPT não definido no .env")

# Detalhes do Projeto

NAME = os.getenv("NAME")
VERSION = os.getenv("VERSION")
DESCRIPTION = os.getenv("DESCRIPTION")

# Configuração da API

HOST = os.getenv("HOST", "0.0.0.0")

try: PORT = int(os.getenv("PORT", 8000)) 
except ValueError: raise ConfigError("PORT deve ser um número inteiro")

RELOAD = os.getenv("RELOAD", "True").lower() == "true"

try: THREADS = int(os.getenv("THREADS", 10))
except ValueError: raise ConfigError("THREADS deve ser um número inteiro")
