"""
Router de itens - define todos os endpoints relacionados a itens
Responsável apenas por receber requisições e retornar respostas
A lógica de negócio fica na camada de serviço
"""

from fastapi import APIRouter
from typing import List, Optional

from app.models import Item, ItemCreate, ItemUpdate
from app.services import ItemService

# Cria o router com prefixo e tags para organização
router = APIRouter(
    prefix="/items",
    tags=["items"]
)


@router.post("", response_model=Item, status_code=201)
def create_item(item: ItemCreate):
    """
    Cria um novo item no supermercado.

    Args:
        item: Dados do item a ser criado

    Returns:
        Item criado com ID gerado
    """
    return ItemService.create_item(item)


@router.get("", response_model=List[Item])
def get_items(item_id: Optional[int] = None):
    """
    Retorna todos os itens ou um item específico.

    Args:
        item_id: (Opcional) ID do item para buscar apenas um

    Returns:
        Lista de itens (todos ou apenas um)
    """
    if item_id is not None:
        return [ItemService.get_item_by_id(item_id)]

    return ItemService.get_all_items()


@router.put("/{item_id}", response_model=Item)
def update_item(item_id: int, item_update: ItemUpdate):
    """
    Atualiza um item existente.

    Args:
        item_id: ID do item a ser atualizado
        item_update: Campos a serem atualizados (todos opcionais)

    Returns:
        Item atualizado
    """
    return ItemService.update_item(item_id, item_update)


@router.delete("/{item_id}")
def delete_item(item_id: int):
    """
    Deleta um item do supermercado.

    Args:
        item_id: ID do item a ser deletado

    Returns:
        Mensagem de confirmação e item deletado
    """
    deleted_item = ItemService.delete_item(item_id)

    return {
        "message": "Item deletado com sucesso",
        "item": deleted_item
    }
