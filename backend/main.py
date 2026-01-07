import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import players, agent
from app.core.config import settings

app = FastAPI(
    title="Power Move API",
    description="Enterprise AI-Powered Baseball Analytics",
    version="1.0.0"
)

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(players.router, prefix="/api/v1/players", tags=["players"])
app.include_router(agent.router, prefix="/api/v1/agent", tags=["agent"])

@app.get("/")
async def root():
    return {
        "message": "Welcome to Power Move API",
        "status": "online",
        "ai_enabled": settings.GOOGLE_API_KEY is not None
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
