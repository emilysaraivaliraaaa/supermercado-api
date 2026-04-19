"""
Módulo de armazenamento em memória
Em produção, isso seria substituído por um banco de dados real (PostgreSQL, MongoDB, etc)
"""

from typing import Dict
from app.models import Item

# Banco de dados em memória
items_db: Dict[int, Item] = {}

# Contador para IDs
_next_id = 1


def get_next_id() -> int:
    """Retorna o próximo ID disponível e incrementa o contador"""
    global _next_id
    current_id = _next_id
    _next_id += 1
    return current_id
