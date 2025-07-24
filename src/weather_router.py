```python
from fastapi import APIRouter, HTTPException
from app.services.weather_service import get_weather_by_city

router = APIRouter()

@router.get("/weather/{city}", tags=["Weather"])
async def read_weather(city: str):
    try:
        weather_data = await get_weather_by_city(city)
        return weather_data
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
```