```python
from fastapi import APIRouter
from app.services import documentation_service

router = APIRouter()

@router.get("/generate-docs", summary="Generate API Documentation")
async def generate_docs():
    return documentation_service.generate_documentation()

@router.get("/generate-readme", summary="Generate README File")
async def generate_readme():
    return documentation_service.generate_readme()
```