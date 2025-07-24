```python
from app.services import example_service
import unittest

class TestExampleService(unittest.TestCase):
    def test_get_item(self):
        self.assertEqual(example_service.get_item(1), {"id": 1, "name": "Item One"})
        self.assertIsNone(example_service.get_item(999))
```