class CustomException(Exception): pass # * Classe base para todas as exceções personalizadas

class ConfigError(CustomException): pass # * Erros de configuração

class FileError(CustomException): pass # * Erros de arquivo

class AIError(CustomException): pass # * Erros da IA

class APIError(CustomException): pass # * Erros da API

