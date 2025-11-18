# source/__init__.py

''' pacote pessoal para funcoes que mexem com pdf '''

from .utils import funcao_1
from .reorder import ordem

__all__ = [
    "ordem",
    "funcao_1", 
    ]

__version__ = "1.0.0"

__name__ = "VivasPdf"