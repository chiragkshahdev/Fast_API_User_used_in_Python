# Day 4 - CRUD Logic API

### 🎯 What I Learned Today
- CRUD = Create, Read, Update, Delete (Backend ka ABCD)
- `fake_db` as In-Memory DB - List ka use
- `HTTPException` - Error handling
- `response_model` - Output control
- Path params `/{item_id}`

### 🔌 API Endpoints
| Method | Endpoint | Work |
|---|---|---|
| POST | /items/ | Create New Item |
| GET | /items/ | Get All Items |
| GET | /items/{id} | Get One Item |
| PUT | /items/{id} | Update Item |
| DELETE | /items/{id} | Delete Item |

### 🧪 Test Data for Swagger
```json
{
  "id": 1,
  "name": "Arc Reactor",
  "price": 9999.99,
  "is_avenger_gear": true
}

pip install fastapi uvicorn
uvicorn main:app --reload