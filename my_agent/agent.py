import os
import requests
import google.generativeai as genai
import google.adk as adk
from google.adk.agents.llm_agent import Agent
from datetime import datetime
from zoneinfo import ZoneInfo


CITY_TO_TZ = {
    "nairobi": "Africa/Nairobi",
    "seattle": "America/Los_Angeles",
    "new york": "America/New_York",
    "london": "Europe/London",
    "tokyo": "Asia/Tokyo",
}

def get_current_time(city: str) -> dict:
    tz = CITY_TO_TZ.get(city.strip().lower())
    if not tz:
        return {
            "error": "Unknown city",
            "supported_cities": list(CITY_TO_TZ.keys())
        }

    now = datetime.now(ZoneInfo(tz))
    return {
        "city": city,
        "timezone": tz,
        "time": now.strftime("%I:%M %p"),
        "datetime": now.isoformat(),
    }


root_agent = Agent(
    model="gemini-2.5-flash"
,
    name='root_agent',
    description='Tells the current time in a specified city.',
    instruction="Ask the user for an IANA timezone (e.g., Africa/Nairobi). Use get_current_time(timezone) to answer.",
    tools =[get_current_time],
)
