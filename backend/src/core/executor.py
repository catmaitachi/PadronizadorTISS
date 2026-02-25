import threading
from concurrent.futures import ThreadPoolExecutor
from src.config import config as env
from src.core.exceptions import APIError

_executor = None
_lock = threading.Lock()

def obter_executor() -> ThreadPoolExecutor:
    
    global _executor

    with _lock:

        if _executor is None:

            try: _executor = ThreadPoolExecutor(max_workers=env.THREADS)
            except Exception as e: raise APIError(f"Erro ao criar pool de threads: {str(e)}") from e

        return _executor
    
def desligar_executor():

    global _executor

    with _lock:

        if _executor is not None:

            _executor.shutdown(wait=True)
            _executor = None