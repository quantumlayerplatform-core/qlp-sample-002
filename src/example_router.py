```python
from fastapi import APIRouter, HTTPException
from app.services import example_service

router = APIRouter()

@router.get("/items/{item_id}", tags=["items"])
async def read_item(item_id: int):
    item = example_service.get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
```