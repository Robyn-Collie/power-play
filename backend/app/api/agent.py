from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.agents.scout import get_scout
from typing import Dict, Any

router = APIRouter()

class AnalysisRequest(BaseModel):
    player_name: str
    stats: Dict[str, Any]

@router.post("/analyze")
async def analyze_player(request: AnalysisRequest):
    try:
        scout = get_scout()
        report = scout.analyze(request.player_name, request.stats)
        return {"report": report}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
