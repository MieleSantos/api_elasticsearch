from fastapi import APIRouter
from router.search_schemas import SearchModel
from db.conection import search
from loguru import logger

router = APIRouter()


@router.post("/search")
async def search_basic(text: SearchModel):
    logger.info(f"Start search with term: {text.text}")
    result = search(text.text)
    return result
