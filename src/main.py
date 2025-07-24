```python
from fastapi import FastAPI
from app.routers import weather_router

app = FastAPI(title="Weather API", description="A modern web application integrating external APIs")

app.include_router(weather_router.router)
```