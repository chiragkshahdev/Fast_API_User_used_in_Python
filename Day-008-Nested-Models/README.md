# Day 8 - Nested Models in FastAPI | Pydantic

Real-world APIs are never flat. They are nested like Amazon, Flipkart.

### 📚 What is Nested Model?

A Pydantic model inside another model.

```python
class Address(BaseModel):...
class User(BaseModel):
    address: Address # <-- Nested