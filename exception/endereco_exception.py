from fastapi import HTTPException, status

endereco_not_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Endereço não encontrado"
)