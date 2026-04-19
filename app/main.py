"""
Entry point da aplicação FastAPI
Responsável por configurar a aplicação e registrar os routers
"""

from fastapi import FastAPI

from app.routers import items_router

# Configuração da aplicação
app = FastAPI(
    title="Supermercado API",
    version="1.0.0",
    description="API REST para gerenciamento de itens de supermercado"
)

# Registra os routers
app.include_router(items_router)


@app.get("/", tags=["health"])
def health_check():
    """Endpoint de health check"""
    return {
        "status": "healthy",
        "message": "API de Supermercado está funcionando"
    }
