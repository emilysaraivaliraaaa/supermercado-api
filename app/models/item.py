from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class ItemCreate(BaseModel):
    """Schema para criação de item"""
    nome: str = Field(..., description="Nome do item", min_length=1)
    preco: float = Field(..., description="Preço do item", gt=0)
    quantidade: int = Field(..., description="Quantidade em estoque", ge=0)
    categoria: str = Field(..., description="Categoria do item")
    marca: str = Field(..., description="Marca do Produto")
    data_validade: date = Field(..., description="Data de validade do produto")
    codigo_barras: Optional[str] = Field(None, description="Código de barras do produto")
    fornecedor: str = Field(..., description="Nome do fornecedor do produto")

    class Config:
        json_schema_extra = {
            "example": {
                "nome": "Arroz",
                "preco": 25.90,
                "quantidade": 100,
                "categoria": "Grãos",
                "marca": "Urbano",
                "data_validade": "2027-12-31",
                "codigo_barras": "7891234567890",
                "fornecedor": "Distribuidora ABC"
            }
        }


class Item(ItemCreate):
    """Schema completo do item com ID"""
    id: int = Field(..., description="ID único do item")

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "nome": "Arroz",
                "preco": 25.90,
                "quantidade": 100,
                "categoria": "Grãos",
                "marca": "Urbano",
                "data_validade": "2027-12-31",
                "codigo_barras": "7891234567890",
                "fornecedor": "Distribuidora ABC"
            }
        }


class ItemUpdate(BaseModel):
    """Schema para atualização parcial de item"""
    nome: Optional[str] = Field(None, description="Nome do item", min_length=1)
    preco: Optional[float] = Field(None, description="Preço do item", gt=0)
    quantidade: Optional[int] = Field(None, description="Quantidade em estoque", ge=0)
    categoria: Optional[str] = Field(None, description="Categoria do item")
    marca: Optional[str] = Field(None, description="Marca do item")
    data_validade: Optional[date] = Field(None, description="Data de validade do produto")
    codigo_barras: Optional[str] = Field(None, description="Código de barras do produto")
    fornecedor: Optional[str] = Field(None, description="Nome do fornecedor do produto")
