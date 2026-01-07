import google.generativeai as genai
from app.core.config import settings
from typing import List, Dict, Any

class BaseScout:
    def analyze(self, player_name: str, stats: Dict[str, Any]) -> str:
        raise NotImplementedError

class GeminiScout(BaseScout):
    def __init__(self):
        genai.configure(api_key=settings.GOOGLE_API_KEY)
        # Updated to use the available model from user's API access
        self.model = genai.GenerativeModel('gemini-2.5-flash')

    def analyze(self, player_name: str, stats: Dict[str, Any]) -> str:
        try:
            prompt = f"""
            You are 'The Scout', an elite AI baseball talent evaluator for an MLB front office.
            Analyze the following stats for {player_name} and provide a concise, high-impact scouting report.
            Focus on exit velocity, consistency, and 'Power Move' potential.
            
            Stats Data: {stats}
            
            Return the report in a professional, slightly gruff tone.
            """
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error calling Gemini: {e}")
            return MockScout().analyze(player_name, stats)

class MockScout(BaseScout):
    def analyze(self, player_name: str, stats: Dict[str, Any]) -> str:
        # High-quality mock responses to show architecture without an API key
        return f"""
        [SIMULATED ANALYSIS FOR {player_name.upper()}]
        
        EYE TEST: Strong frame, disciplined approach at the plate.
        DATA BREAKDOWN: Barrel percentage is in the 90th percentile. We're seeing a consistent launch angle that suggests sustainable power.
        THE POWER MOVE: If he keeps his weight back on the off-speed stuff, he's a 40-HR threat. 
        VERDICT: Must-have for the 2026 roster.
        
        (Note: Real AI analysis is currently in 'Sandbox Mode' because the API Key is not configured or reachable.)
        """

def get_scout() -> BaseScout:
    if settings.GOOGLE_API_KEY and not settings.GOOGLE_API_KEY.startswith("your_"):
        try:
            return GeminiScout()
        except Exception:
            return MockScout()
    return MockScout()
