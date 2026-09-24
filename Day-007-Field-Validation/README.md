# Day 7 - Field Validation in FastAPI | Pydantic

Validation is what makes FastAPI better than Flask/Django REST. Client can never send bad data.

### 📚 Validations Covered

#### 1. Field() Parameters
| Param | Use | Example |
| :--- | :--- | :--- |
| `min_length`, `max_length` | String length | `min_length=3` |
| `gt`, `ge`, `lt`, `le` | Number range | `gt=0` ( > 0), `ge=18` ( >=18) |
| `regex` | Pattern matching | `^[A-Z]{3}-[0-9]{4}$` |
| `min_items`, `max_items` | List size | For tags |
| `EmailStr` | Email auto validate | Built-in |
| `HttpUrl` | URL auto validate | Built-in |

#### 2. Custom @validator
- Password strength (Uppercase + Number + Special char)
- Confirm password matching
- Phone number regex
- DOB not in future
- Age vs DOB cross-check

### 🔥 Try These in /docs (They will FAIL)

```json
{
  "name": "ab",
  "email": "not-an-email",
  "password": "weak",
  "confirm_password": "different",
  "age": 15,
  "dob": "2030-01-01",
  "phone": "123"
}