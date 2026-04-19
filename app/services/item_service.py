"""
Camada de serviço - contém a lógica de negócio
Separa a lógica dos endpoints (routers) e acesso aos dados (database)
"""

from typing import List, Optional
from fastapi import HTTPException

from app.models import Item, ItemCreate, ItemUpdate
from app.database import items_db, get_next_id


class ItemService:
    """Serviço para gerenciar operações de itens"""

    @staticmethod
    def create_item(item_data: ItemCreate) -> Item:
        """
        Cria um novo item no banco de dados

        Args:
            item_data: Dados do item a ser criado

        Returns:
            Item criado com ID gerado
        """
        item_id = get_next_id()

        new_item = Item(
            id=item_id,
            nome=item_data.nome,
            preco=item_data.preco,
            quantidade=item_data.quantidade,
            categoria=item_data.categoria
        )

        items_db[item_id] = new_item
        return new_item

    @staticmethod
    def get_all_items() -> List[Item]:
        """
        Retorna todos os itens cadastrados

        Returns:
            Lista de todos os itens
        """
        return list(items_db.values())

    @staticmethod
    def get_item_by_id(item_id: int) -> Item:
        """
        Busca um item pelo ID

        Args:
            item_id: ID do item a ser buscado

        Returns:
            Item encontrado

        Raises:
            HTTPException: Se o item não for encontrado
        """
        if item_id not in items_db:
            raise HTTPException(
                status_code=404,
                detail=f"Item com ID {item_id} não encontrado"
            )

        return items_db[item_id]

    @staticmethod
    def update_item(item_id: int, item_update: ItemUpdate) -> Item:
        """
        Atualiza um item existente

        Args:
            item_id: ID do item a ser atualizado
            item_update: Dados para atualização (campos opcionais)

        Returns:
            Item atualizado

        Raises:
            HTTPException: Se o item não for encontrado
        """
        if item_id not in items_db:
            raise HTTPException(
                status_code=404,
                detail=f"Item com ID {item_id} não encontrado"
            )

        stored_item = items_db[item_id]

        # Atualiza apenas os campos fornecidos
        update_data = item_update.model_dump(exclude_unset=True)
        updated_item = stored_item.model_copy(update=update_data)

        items_db[item_id] = updated_item

        return updated_item

    @staticmethod
    def delete_item(item_id: int) -> Item:
        """
        Deleta um item do banco de dados

        Args:
            item_id: ID do item a ser deletado

        Returns:
            Item deletado

        Raises:
            HTTPException: Se o item não for encontrado
        """
        if item_id not in items_db:
            raise HTTPException(
                status_code=404,
                detail=f"Item com ID {item_id} não encontrado"
            )

        deleted_item = items_db.pop(item_id)

        return deleted_item
