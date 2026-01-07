from fastapi import APIRouter, HTTPException
import requests
from app.core.config import settings

router = APIRouter()

@router.get("/search")
async def search_players(name: str):
    try:
        url = f"{settings.MLB_API_BASE_URL}/people/search?names={name}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{player_id}/stats")
async def get_player_stats(player_id: int):
    try:
        # Fetch current season AND year-by-year history for analytics
        url = f"{settings.MLB_API_BASE_URL}/people/{player_id}?hydrate=stats(group=[hitting,pitching],type=[season,yearByYear])"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
